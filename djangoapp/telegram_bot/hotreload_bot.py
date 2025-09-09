import os
import subprocess
import sys
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


class ReRunner(PatternMatchingEventHandler):
    patterns = ["bot.py"]  # Extensões dos arquivos a serem monitorados

    def __init__(self, command):
        super(ReRunner, self).__init__()
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)
        self.self_pid = os.getpid()

    def on_modified(self, event):
        self.restart()

    def find_process(self):
        """ Função para encontrar processos pelo nome do comando. """
        try:
            # Lista processos que correspondem ao nome do script
            output = subprocess.check_output(['pgrep', '-f', self.command])
            pids = [int(pid) for pid in output.split() if int(pid) != self.self_pid]
            print(pids)
            return pids
        except subprocess.CalledProcessError:
            print('Se "pgrep" não encontrar o processo, retorna lista vazia')
            return []

    def kill_process(self, pids):
        for pid in pids:
            try:
                ReRunner(command=f'kill -9 {pid}')
                time.sleep(1)  # Dá um tempo para o processo encerrar
                if os.path.exists(f"/proc/{pid}"):  # Verifica se o processo ainda está ativo
                    ReRunner(command=f'kill -9 {pid}')  # Força o término se ainda estiver ativo
                    print(f"Processo {pid} forçado a encerrar.")
                else:
                    print(f"Processo {pid} encerrado com SIGTERM.")
            except OSError:
                pass

    def restart(self):
        pids = self.find_process()
        self.kill_process(pids)
        time.sleep(1)
        self.process = subprocess.Popen(self.command, shell=True)

def run_script():
    command = 'python bot.py'
    event_handler = ReRunner(command=command)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    run_script()

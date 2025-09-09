// document.addEventListener("DOMContentLoaded", function() {})
let handlePWAModal = function (){
  if (!window.matchMedia('(display-mode: standalone)').matches) {
      setTimeout(function(){
        jQuery('.pwa-offcanvas').addClass('show');
        jQuery('.pwa-backdrop').addClass('fade show');
      }, 3000);
      jQuery('.pwa-backdrop, .pwa-close, .pwa-btn').on('click',function(){
        jQuery('.pwa-offcanvas').slideUp(500, function() {
          jQuery(this).removeClass('show');
        });
        setTimeout(function(){
          jQuery('.pwa-backdrop').removeClass('show');
        }, 500);
      });
  }
}

let isPWA = false;
let isMobile = /Android/i.test(navigator.userAgent);
let isIphone = false

window.addEventListener('appinstalled', (evt) => {
  isPWA = true;
});

const isIos = () => {
  const userAgent = window.navigator.userAgent.toLowerCase();  
  return /iphone|ipad|ipod/.test( userAgent );
}

const isInStandaloneMode = () => ('standalone' in window.navigator) && (window.navigator.standalone);


if (!isPWA && isMobile) {
  const modal = document.getElementById('showAlertPWA');
  if (modal){
    modal.style.display = "block"
    handlePWAModal()
  }
}

if (isIos() && !isInStandaloneMode()) {
  const modal = document.getElementById('showAlertPWAIos');
  isIphone = true
  if (modal){
    modal.style.display = "block";
    handlePWAModal()
  }
}

document.addEventListener("DOMContentLoaded", function() {
  let isMovel = false;      
  let displayMode = false;
  if (navigator.userAgent.match(/mobile/i)) {
      isMovel = true;
      if (window.matchMedia('(display-mode: standalone)').matches) {
        displayMode = true;
      }
  }    
  document.body.setAttribute('isPWA', displayMode);
  document.body.setAttribute('isIphone', isIphone);
  document.body.setAttribute('isMobile', isMovel);
  const sendCount = document.querySelector('.sendCountPlatform');
  if(sendCount){
    htmx.trigger(sendCount, 'load');
  }
  
});    



window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  let deferredPrompt = e;
  if (!isPWA && isMobile) {
    const installButton = document.getElementById('install-pwa');
    // installButton.style.display = "block";

    installButton.addEventListener('click', (e) => {
      installButton.style.display = "none";

      deferredPrompt.prompt();

      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('Usuário aceitou a instalação');
        } else {
          console.log('Usuário recusou a instalação');
        }
        deferredPrompt = null;
      });
    });
  }
});

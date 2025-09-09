from chat.utils.creat_finetune import list_models
from chat.utils.upload_s3 import generate_and_upload_jsonl
from django.http import HttpResponse


def export(request, *args, **kwargs):
    # generate_and_upload_jsonl()
    list_models()
    return HttpResponse('Export')

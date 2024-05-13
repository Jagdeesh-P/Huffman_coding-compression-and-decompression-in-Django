from django.shortcuts import render
from django.http import HttpResponse
from .huffman import HuffmanCoding


def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        text_file = request.FILES['file']
        text = text_file.read().decode('utf-8')
        huffman = HuffmanCoding(text)
        compressed_data = huffman.compress()

        with open('compressed_file.bin', 'wb') as f:
            f.write(compressed_data)

        decompressed_text = huffman.decompress(compressed_data)
        with open('decompressed_file.txt', 'w') as f:
            f.write(decompressed_text)

        return render(request, 'download.html')

    return render(request, 'upload.html')


def download_compressed(request):
    with open('compressed_file.bin', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="compressed_file.bin"'
    return response


def download_decompressed(request):
    with open('decompressed_file.txt', 'r') as f:
        response = HttpResponse(f.read(), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="decompressed_file.txt"'
    return response

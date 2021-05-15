import requests
TOKEN = ''

class YaUploader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {TOKEN}'}

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self):
        href = self._get_upload_link(disk_file_path=f'/{self.file_path}').get("href", "")
        response = requests.put(href, data=open("File.txt", 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    uploader = YaUploader(r'Projects\1.9 Requests\File.txt')
    result = uploader.upload()


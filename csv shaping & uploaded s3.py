import os
import boto3

# Configuration
s3 = boto3.client('s3')
bucket = 'demoencryption'  # <-- change this!
parent_folder = 'Cleaned_data'
work_dir= '/Users/chloe/Desktop/Banana_project/Cleaned_data'

files = [
    f for f in os.listdir(work_dir)
    if f.endswith('.csv') and os.path.isfile(os.path.join(work_dir, f))
]

# Function to re-encode & upload
def upload_utf8_files():
    for file in files:
        folder = file.replace('.csv', '')  # folder name = file name without extension
        utf8_file = f'utf8_{file}'
        print(f" Processing {file} → {utf8_file}")

        # re-save file as UTF-8
        with open(os.path.join(work_dir, file), 'r', encoding='utf-8', errors='replace') as fin, \
             open(utf8_file, 'w', encoding='utf-8') as fout:
            fout.write(fin.read())

        s3_key = f"{parent_folder}/{folder}/{file}"
        s3.upload_file(utf8_file, bucket, s3_key)
        print(f" Uploaded to s3://{bucket}/{s3_key}")
        os.remove(utf8_file)

if __name__ == '__main__':
    upload_utf8_files()

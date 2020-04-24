from pyresparser import ResumeParser


def get_resume_data(file):
    data = ResumeParser(f"socialapp/static/upload/{file}").get_extracted_data()
    return data

# print(get_resume_data('/home/fission/Downloads/resume.pdf'))
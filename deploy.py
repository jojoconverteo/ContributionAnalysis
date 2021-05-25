import os

def deploy_streamlit_app():
    step_1 = "gcloud auth login"
    step_2 = "gcloud init"
    step_3 = "gcloud app deploy"
    step_4 = "gcloud app browse"
    all_step = [step_1, step_2, step_3, step_4]
    for step in all_step:
        os.system(step)

if __name__ == "__main__":
    deploy_streamlit_app()
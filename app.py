# Python Libraries 
import pandas as pd
from fastapi import FastAPI

# UI Libraries
import gradio as gr

app = FastAPI()

def pycaret_process(file_path):
    dataset = pd.read_csv(file_path)
    target_column = "SalePrice"
    #r = RegressionExperiment()
    #filtered_features = dataset.loc[:, dataset.columns != target_column]
    #filtered_dataset = pd.DataFrame(filtered_features, columns=filtered_features.columns)
    #clf = r.setup(filtered_dataset, target=dataset[target_column],preprocess=False,transformation= False, session_id=2, experiment_name ='Regression',index=False)
    #best_model = clf.compare_models(fold=5,exclude = ['lightgbm','qda','dummy','ridge','catboost','br','et','lasso','huber','llar'])
    best_model="Unable Fetch"
    return gr.Textbox(label="Best Model",value=best_model,visible=True)

with gr.Blocks(title="SE FSTool") as FSTool:
    gr.Markdown("<span style='color: black;'>Please upload a CSV file</span>",sanitize_html=True)    
    with gr.Row():
        with gr.Column():  
            file_input = gr.File(label="Upload Dataset",file_types=['.csv'],file_count="single")  
            apply_button = gr.Button("Start Process",visible=True)
            best_model = gr.Textbox(label="Best Model")
            apply_button.click(pycaret_process,inputs=[file_input],outputs=[best_model])

app = gr.mount_gradio_app(app, FSTool, path="/")

# Langchain RAG Tutorial

## Install dependencies

1. Do the following before installing the dependencies found in `requirements.txt` file because of current challenges installing `onnxruntime` through `pip install onnxruntime`. 

    - For MacOS users, a workaround is to first install `onnxruntime` dependency for `chromadb` using:

    ```python
     conda install onnxruntime -c conda-forge
    ```
    See this [thread](https://github.com/microsoft/onnxruntime/issues/11037) for additonal help if needed. 

     - For Windows users, follow the guide [here](https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file) to install the Microsoft C++ Build Tools. Be sure to follow through to the last step to set the enviroment variable path.


2. Now run this command to install dependenies in the `requirements.txt` file. 




```python
pip install -r requirements.txt
```


## Create database

Create the Chroma DB.

```python
python create_database.py
```



-----------------------------------------------
python app.py            (to start ui)
-----------------------------------------------




## Query the database

Query the Chroma DB.




examlpes of queries for "Dalili" project:

```python
python query_data.py "what is the best practice to prevent overfitting and underfitting?" #pass
python query_data.py "Explain all steps of CNN" #Pass
python query_data.py "what is the difference between Gradiant Boosting and Linear regression?"  #pass
python query_data.py "how can i handle null values?" # pass 10/10
python query_data.py "what is the different between precision and recall?"
python query_data.py "What is the difference between PCA and UMAP" #pass
python query_data.py "what is the affect of high and low entropy?" #pass (mentioned once)
python query_data.py "who is trump?" #pass (mentioned once)

```

> You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.

Here is a step-by-step tutorial video: [RAG+Langchain Python Project: Easy AI/Chat For Your Docs](https://www.youtube.com/watch?v=tcqEUSNCn8I&ab_channel=pixegami).

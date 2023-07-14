# About

Please check out my blog about this repo [here](https://harrywang.me/mvp).

This is my revised version of the sample chatbot kickstarter provided by OpenAI at https://github.com/openai/openai-cookbook/tree/main/apps/chatbot-kickstarter, which shows how you can create apps using ChatGPT and your own data.

This sample app shows a common architecture used for many ChatGPT-based apps, which I want to call:

> MVP: M (Large Language Model) + V (VectorDB) + P (Prompt Engineering)

If a fine-tuned LLM is used, then it is FMVP (Fine-tuned MVP).

Changes I made:

- Added OpenAI API key loading
- Changed the datasets
- Added more instructions and made code changes

## Data

I used new data files as follows for the examples:

- [NBA Official Rulebook 2022-23 ](https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2022/10/Official-Playing-Rules-2022-23-NBA-Season.pdf)
- [IFAB (International Football Association Board) Laws of the Game 2023-2024](https://www.theifab.com/laws-of-the-game-documents/) - I removed all images in the PDF to reduce the file size.

If you want to use other data, just put the PDF files in `data` folder.

## Get Started

- Install Docker and run the following command to start a local Redis database:

```
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

- Create a `.env` file and include your OpenAI API key:

```
OPENAI_API_KEY=sk-xxxx
```

- Setup the virtual environment and install the packages:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Run the `mvp.ipynb` file to go over the key steps to build starter Q&A and Chatbot applications using the ChatGPT API and their own data. 

- Run Streamlit apps (Q&A and Chat):


```
streamlit run app-search.py
```

or 

```
streamlit run app-chat.py
```
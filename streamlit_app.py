from datasets import load_dataset
import streamlit as st

dataset = load_dataset("merve/poetry", streaming=True)
df = pd.DataFrame.from_dict(dataset["train"])

st.write("Most appearing words including stopwords")
st.bar_chart(words[0:50])

st.write("Number of poems for each author")
sns.catplot(x="author", data=df, kind="count", aspect = 4)
plt.xticks(rotation=90)
st.pyplot()

import streamlit as st 
st.title('Sentiment Analysis')

df["Sentiment"] = Store

df
select = st.text_input('Enter text')
s=vs.polarity_scores(select)
result = ''
flag=0
#st.title(result)
if s['compound'] > 0 : 
  result='The news contains a positive sentiment'
  flag=flag+1
elif s['compound'] < 0 :
  result='The news contains a negetive sentiment'
  flag=flag+1
elif s['compound'] == 0 :
  result='The news contains a neutral sentiment'
  flag=flag+1
#st.title
#if flag>1:
st.title(result)

# -*- coding: utf-8 -*-

import streamlit as st

def main():
    st.title('This is Text Elements')
    st.header('This is 헤더')
    st.subheader('This is sub Header')
    st.write('파이썬 문법 사용 가능')
    
    st.markdown("""
    ### SubChapter 1.
    - 피타고라스 정리: :red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:            
    """)

if __name__=='__main__':
    main()
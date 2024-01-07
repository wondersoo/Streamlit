# -*- coding: utf-8 -*-

import streamlit as st

def main():
    st.markdown('HTML CSS 마크다운 적용')
    html_css = """
    <thead>
        <tr>
         <th>Header 1</th>
         <th>Header 2</th>
         <th>Header 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
         <td>Row 1, Cell 1</td>
         <td>Row 1, Cell 2</td>
         <td>Row 1, Cell 3</td>
        </tr>
        <tr>
         <td>Row 2, Cell 1</td>
         <td>Row 2, Cell 2</td>
         <td>Row 2, Cell 3</td>
        </tr>
        <tr>
         <td>Row 3, Cell 1</td>
         <td>Row 3, Cell 2</td>
         <td>Row 3, Cell 3</td>
        </tr>
        <tr>
         <td>Row 4, Cell 1</td>
         <td>Row 4, Cell 2</td>
         <td>Row 4, Cell 3</td>
        </tr>
     </tbody>
    </table>
    """

    st.markdown(html_css, unsafe_allow_html=True)

if __name__=='__main__':
    main()
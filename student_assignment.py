
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter, RecursiveCharacterTextSplitter)
import re 
q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    # 使用 PyPDFLoader 加載 PDF
    loader = PyPDFLoader(q1_pdf)

    # 讀取 PDF 內容
    documents = loader.load()
    #documents 是一個 Document 對象的列表，每個 Document 包含：
    #.page_content：該頁的純文本內容
    #.metadata：包含 source 和 page 等資訊   

    # 使用 CharacterTextSplitter 將文本以頁為單位分割為多個 chunks
    # 設定文本分割器
    TextSplitterHandler = CharacterTextSplitter(chunk_overlap=0)
    # chunk_overlap=0 的意思是在使用 CharacterTextSplitter 切割文本時，
    #不會在相鄰的區塊 (chunks) 之間保留重疊的內容。這表示每個 chunk 都是完全獨立的，不會有重複的字元。

    # 用 split_text 或是 split_documents 得到分割後的chunk。
    chunks = TextSplitterHandler.split_documents(documents)
   
    # 顯示分割後的 chunks
    """
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk.page_content}\n{'-'*50}")
    """

    # 回傳最後一個 chunk 物件
    return chunks[-1]

def hw02_2(q2_pdf):
    pass

def hw02_2(q2_pdf):

    # 使用 PyPDFLoader 加載 PDF
    loader = PyPDFLoader(q2_pdf)

    # 讀取 PDF 內容
    documents = loader.load()

    # 合併文件大段落
    Full_Doc = "\n".join([doc.page_content for doc in documents])
    # check full_text
    """
    # print(full_text)
    """
    #separators = [r"\s*第\s*[\u4e00-\u9fa5]+\s*章\s*", r"\s*第\s*\d+(-\d+)?\s*條\s*\n"],
    DocSeparators=[r"第\s+.*\s+章\s+", r"第\s+.*\s+條\s+",]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 5, 
    chunk_overlap = 0, 
    separators = DocSeparators, 
    is_separator_regex = True)

    Doc_text = text_splitter.split_text(Full_Doc)

    for i in range(5):
        print("-"*10)
        print(Doc_text[i])

    return len(Doc_text)


# Self Test
"""
last_chunk = hw02_1(q1_pdf)
print(last_chunk)
#"""

"""
chunks_count = hw02_2(q2_pdf)
print(f"Total number of chunks: {chunks_count}")
#"""
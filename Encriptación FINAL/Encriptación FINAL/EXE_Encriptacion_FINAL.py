from distutils.core import setup 
import py2exe 
 
setup(name="ENCRIPTADOR", 
 version="1.0", 
 description="ENCRIPTA con CESAR y VIGENERE", 
 author="GRUPO 2 TER - UOC - 2020_1-2020_2", 
 author_email="mmarmol@uoc.edu", 
 url="https://sites.google.com/uoc.edu/intermedios", 
 license="Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)", 
 scripts=["Encriptación_FINAL.py", 
 console=["Encriptación_FINAL.py", 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)
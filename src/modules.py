

import tkinter as tk  # biblioteca GUI      
from tkinter import *  # importando todas as propriedade do tkinter
from tkinter import ttk
from tkinter import messagebox, scrolledtext, Menu
from tkinter import PhotoImage
from tkcalendar import Calendar, DateEntry
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser 
import requests
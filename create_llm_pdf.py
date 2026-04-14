#!/usr/bin/env python3
"""Create a PDF document with Large Language Models content."""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_path = "data/Large_Language_Models_Guide.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1f4788'),
    spaceAfter=30,
    alignment=1  # Center
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#2563eb'),
    spaceAfter=12,
    spaceBefore=12
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=11,
    alignment=4,  # Justify
    spaceAfter=12
)

# Content
elements = []

# Title
elements.append(Paragraph("Large Language Models (LLMs)", title_style))
elements.append(Paragraph(f"Comprehensive Guide • {datetime.now().strftime('%B %Y')}", styles['Normal']))
elements.append(Spacer(1, 0.3*inch))

# Introduction
elements.append(Paragraph("Introduction", heading_style))
intro_text = """
A Large Language Model (LLM) is a computational model designed to perform natural language processing tasks, 
especially language generation, using contextual relationships derived from a large set of training data. LLMs can 
generate, summarize, translate and parse text in a variety of contexts, and are the technological underpinning of 
modern chatbots. They can accurately mimic natural language patterns because they are trained on collections of 
human-written text.
"""
elements.append(Paragraph(intro_text, normal_style))
elements.append(Spacer(1, 0.2*inch))

# Architecture
elements.append(Paragraph("Architecture", heading_style))
arch_text = """
As of 2024, the largest and most capable LLMs are all based on transformer architectures, which can be more 
efficient and parallelizable than earlier statistical and recurrent neural network models. The transformer 
architecture leverages an attention mechanism that enables the model to process relationships between all 
elements in a sequence simultaneously, regardless of their distance from each other.
"""
elements.append(Paragraph(arch_text, normal_style))
elements.append(Spacer(1, 0.2*inch))

# Key Components
elements.append(Paragraph("Key Components", heading_style))

components_data = [
    ["Component", "Description"],
    ["Tokenization", "Converting text into tokens for processing (Byte-Pair Encoding, WordPiece)"],
    ["Attention Mechanisms", "Allows the model to focus on relevant parts of input"],
    ["Parameters", "Typically billions - GPT-3 has 175 billion parameters"],
    ["Context Window", "Maximum amount of text the model can consider at once"],
    ["Embeddings", "Vector representations of tokens that capture semantic meaning"]
]

table = Table(components_data, colWidths=[1.5*inch, 4.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563eb')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
]))
elements.append(table)
elements.append(Spacer(1, 0.2*inch))

# Training
elements.append(Paragraph("Training Process", heading_style))
training_text = """
LLMs are typically trained in two stages: pretraining and fine-tuning. During pretraining, models learn from 
massive amounts of text data to predict the next word in a sequence. Fine-tuning then adapts the model for 
specific tasks using techniques like Reinforcement Learning from Human Feedback (RLHF) or instruction fine-tuning.
The training of large models requires substantial computational resources and can cost millions of dollars.
"""
elements.append(Paragraph(training_text, normal_style))
elements.append(Spacer(1, 0.2*inch))

# Capabilities
elements.append(Paragraph("Key Capabilities", heading_style))
capabilities_text = """
<b>•  Text Generation:</b> Creating coherent, contextually relevant text<br/>
<b>•  Summarization:</b> Condensing long documents into key points<br/>
<b>•  Translation:</b> Converting text between languages<br/>
<b>•  Question Answering:</b> Finding and formulating answers from context<br/>
<b>•  Reasoning:</b> Some models can perform multi-step logical reasoning<br/>
<b>•  Code Generation:</b> Writing and debugging computer code<br/>
<b>•  Zero-shot Learning:</b> Performing tasks without specific training examples
"""
elements.append(Paragraph(capabilities_text, normal_style))
elements.append(Spacer(1, 0.2*inch))

# Limitations
elements.append(Paragraph("Limitations and Challenges", heading_style))
limitations_text = """
<b>Hallucinations:</b> LLMs can generate plausible but factually incorrect information.<br/>
<b>Bias:</b> Training data biases can manifest in model outputs, affecting different demographic groups.<br/>
<b>Context Length:</b> Models have limited context windows, restricting their ability to process very long documents.<br/>
<b>Energy Consumption:</b> Training and running large models requires substantial computational resources.<br/>
<b>Interpretability:</b> Understanding why models make specific decisions remains challenging.
"""
elements.append(Paragraph(limitations_text, normal_style))
elements.append(Spacer(1, 0.2*inch))

# Applications
elements.append(Paragraph("Real-World Applications", heading_style))
applications_text = """
LLMs power modern chatbots like ChatGPT and Claude, enable code completion tools such as GitHub Copilot, 
assist in content creation, support customer service automation, enable document analysis and retrieval systems, 
and enhance search functionality. They are increasingly used in healthcare, legal, financial, and educational sectors.
"""
elements.append(Paragraph(applications_text, normal_style))

# Build PDF
doc.build(elements)
print(f"✓ PDF created successfully: {pdf_path}")

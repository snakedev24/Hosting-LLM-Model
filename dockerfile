# Use an appropriate base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
RUN pip install -r python/requirements.txt

COPY python/llm.py .
COPY python/app.py .
COPY templates templates

# Set environment variables (optional)
ENV HF_HOME /root/.huggingface
ENV HF_TOKEN <Enter your huggingface token >

EXPOSE 7000

# Command to run the Python script
# CMD ["python","app.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

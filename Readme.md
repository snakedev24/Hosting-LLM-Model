# Flask LLM Text Generation Application

This Flask application allows you to generate text using the llama-3-8b Large Language Model (LLM) provided by Hugging Face's Transformers library. The LLM model is fine-tuned for text generation tasks and can produce coherent and contextually relevant responses based on prompts provided by the user.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- Hugging Face Transformers
- Torch

#### Docker Setup flow:


1. **Visit Docker's Official Website:**
   Go to [Docker's official website](https://www.docker.com/get-started) to download the Docker Desktop application for your operating system (Windows/Mac/Linux).

2. **Download Docker Desktop:**
   - For Windows and Mac users, download the Docker Desktop installer from the website.
   - For Linux users, follow the instructions provided on the website to install Docker using the appropriate package manager for your distribution.

3. **Install Docker Desktop:**
   - For Windows: Double-click on the downloaded installer and follow the on-screen instructions to complete the installation.
   - For Mac: Drag and drop the Docker icon into your Applications folder, then open Docker from Launchpad or Spotlight.
   - For Linux: Follow the installation instructions provided on the Docker website for your specific Linux distribution.

4. **Launch Docker Desktop:**
   Once Docker Desktop is installed, launch the application. You may need to sign in with your Docker Hub account or create a new one if prompted.

5. **Verify Installation:**
   After launching Docker Desktop, open a terminal or command prompt and run the following command to verify that Docker is installed and running correctly:

### Follow the below commands to setup the project in Docker:

#### Dockerfile Configuration

1. **Open the Dockerfile:**
   Open your Dockerfile in a text editor.

   ```dockerfile
   ENV HF_TOKEN <Enter your Hugging Face token>
   # Example:
   # ENV HF_TOKEN Rslj233ljfsdf

   EXPOSE <Enter Port No>
    # Example:
    # EXPOSE 5000

    Important Commands run one time only

    # docker build -t <image_name> .
    # docker run -p 5000:5000 <image_name>

    To run your Docker container again, use the following command:
    # docker run <Container ID>


    









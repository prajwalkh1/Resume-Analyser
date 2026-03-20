from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found. Check your .env file")

print("DEBUG KEY:", api_key)

client = genai.Client(api_key=api_key)


def analyse_resume_gemini(resume_content, job_description):

    prompt = f"""You are an expert HR recruiter and resume analyzer.

Compare the following resume with the job description.

RESUME:
{resume_content}

JOB DESCRIPTION:
{job_description}

Provide analysis in this format:

Match Score: (0–100)

Missing Skills:
- skill 1
- skill 2

Suggestions:
- suggestion 1
- suggestion 2

Summary:
Short explanation about candidate suitability.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        try:
            return response.text
        except:
            return str(response)

    except Exception as e:
        return f"❌ Error analyzing resume: {str(e)}"
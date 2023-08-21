# !!! THIS IS USED AS A DEMO ONLY REPO TO TEST MY AGENT !!!
An old, non-significant repo I use to demonstrate some of the concepts for lablab.ai Autonomous AI Agent hackathon.
```I do not recommend to run or use it in production.```

One of the interesting aspects here is the test report: [HERE](report.html)

```In a real-life scenario, such tests and reports would be run automatically inside some CI/CD pipeline. This is for demo purposes only.```

# Next gen CV assistant:

**The problem:** the process of applying for a job, creating a CV, going through interviews is not a simple process, especially for people with visual impairments. As an applicant, it is important to fully present oneself as they are, their skills and competences so that it is easier for employers to decide whether their company is a good match.

This assistant allows for audio input from the user (voice) and based on the user’s speech, it generates a CV (curriculum vitae). It uses Whisper for voice recognition and ChatGPT / GPT3 for paraphrasal and formation of structured text CV.

## Running app

1. Create an `.env` file with your `OPENAI_KEY`
2. Run the app using `flask run`

# ECT AI Access

## Goals

- Choose an AI resource that fits your project's data and where it must run
- Create an API key and get a first answer from your own code

## Resources

- Personal Computer (Desktop or Laptop)
- OHIO account

## Environmental Context

- OU campus network for the ECT AI-01 server
- Any internet connection for the cloud options

## At a glance

Start on the ECT AI-01 server: it is free, keeps your data on campus, and uses the same API as most options below. You can switch later by changing three settings (Building the project, below).

| Option | Cost to you | Callable from your code | Works off campus | Where your prompts go | Setup time |
| --- | --- | --- | --- | --- | --- |
| ECT AI-01 Server (On Prem) | Free | Yes, OpenAI-compatible API | No, OU campus network only | An ECT server on campus | Sign in through Izzy |
| Microsoft Copilot Chat (OHIO login) | Free | No, chat only | Yes | Microsoft, under OHIO's license | Minutes |
| GitHub Copilot Student | Free | No, coding help in your editor | Yes | GitHub | Days (student verification) |
| Azure for Students | $100 credit, 12 months | Yes | Yes | Microsoft Azure | An hour, 18 or older |
| Gemini API free tier | Free, rate limited | Yes, OpenAI-compatible (beta) | Yes | Google; free-tier prompts may be read and reused | Minutes, 18 or older |

Plan on AI-01 for the real work and demo, and a cloud option for anything that must run off campus.

## Ground rules

Send AI tools only public, low-impact or made-up data. That is OHIO's rule for every AI tool except the protected Copilot ([Secure Use of AI Tools standard](https://www.ohio.edu/oit/security/policy-practices/consulting/standards/secure-use-artificial-intelligence-tools)).

- **Never send** student records, grades, health or payment data, passwords, or anyone's personal information. Build with sample data you invent.
- **Keep API keys secret.** Not in code, screenshots, chat logs or Git. If a key leaks, delete it and make a new one.
- **Use AI in coursework only as your instructor allows**, and say in your write-up which tools you used and for what.
- **Check every answer.** Models state wrong facts confidently; your project should not pass them on unchecked.
- **No AI images for university marketing**, OHIO social media or ohio.edu ([AI cybersecurity guidance](https://www.ohio.edu/oit/security/ai-cybersecurity-awareness-guidance)).
- **Sent sensitive data by mistake?** Tell security@ohio.edu or call 740-566-7233 right away.

## ECT AI-01 Server (On Prem)

AI-01 is an ECT server on campus that runs open AI models behind Open WebUI, a ChatGPT-style site that also has an API. It is free to use and reachable only from the OU campus network.

- **How to open it:** the **AI-01 Ollama/Open WebUI** tile in Izzy at https://izzy.its.ohio.edu. Your code calls its API at http://ai-01.its.ohio.edu/api.
- **Hardware:** one NVIDIA A10 GPU with 24 GB of memory.
- **Your model:** gemma4:26b, which also reads images. It is the only model student accounts can use.
- **Longest prompt:** 32,768 tokens.

`GET /api/models` confirms which models your account can use.

### Getting access

1. On campus, sign in at https://izzy.its.ohio.edu and open the **AI-01 Ollama/Open WebUI** tile. On the page it opens, choose **Continue with Ohio University**; you should see gemma4:26b.
2. Your new account sees no models yet? Sign out of Izzy and of Open WebUI, then sign in to Izzy again and reopen the tile, because access is picked up at sign-in. If that doesn't work, email the server admin (this guide's author).
3. For the API, open **Settings > Account > API keys** and create a key.

### Using it well

- **It is shared** by staff, campus apps and other students. No loops or load tests; ask first if you expect more than a few hundred calls a day.
- **It is slower than cloud AI.** Set your client timeout to 120 seconds or more, and stream long answers.
- **Use gemma4:26b.** It is the only model student accounts can reach; asking the API for any other returns "Model not found".
- **Stay under the prompt limit.** A longer prompt is cut silently, often losing your system prompt, and the server still reports success. Trim old chat turns.
- **Reasoning is separate.** If the model thinks before answering, it returns that thinking in `message.reasoning_content` and the answer in `message.content`.
- **Web search and the built-in tools are chat-site features.** Through the API you get the plain model.
- **There is no uptime promise.** The server restarts for updates, so keep a fallback ready for demo day.

## OHIO Student Cloud AI Servers (Off-Prem)

OHIO gives every student Microsoft Copilot Chat with GPT-5 at no cost, but it is a chat site with no API, so it helps you plan and learn, not run inside your project ([OHIO news, October 2025](https://www.ohio.edu/news/2025/10/microsoft-copilot-now-running-gpt-5)).

- **Sign in** at https://copilot.microsoft.com with your OHIO email. A green shield means you are in the protected version.
- **It is the only AI tool OHIO approves for sensitive data** ([standard](https://www.ohio.edu/oit/security/policy-practices/consulting/standards/secure-use-artificial-intelligence-tools)). Your project still should not need any.
- **Good uses:** brainstorming features, explaining an error message, drafting requirements from user needs, reviewing your write-up.
- **Not included:** Copilot inside Word, Excel or PowerPoint is not part of OHIO's student license.

## Free student offers from vendors

Three vendor offers matter here: GitHub Copilot Student helps you write code, Azure for Students gives you a cloud API on your own $100 credit, and the Gemini free tier gives you a quick cloud API for public data.

### GitHub Copilot Student

- **Free for verified students.** Apply at https://github.com/settings/education/benefits, then activate Copilot Student; activation can take several days ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)).
- **Since June 2026** it includes 200 AI credits a month plus unlimited code completions, and it chooses the model for you ([GitHub announcement](https://github.com/orgs/community/discussions/189268)).
- **It writes code with you; it is not an API your project calls.** The same [Student Developer Pack](https://education.github.com/pack) also carries the Azure credit below and some hosting credits.

### Azure for Students

- **$100 of credit for 12 months, no credit card.** For full-time students 18 or older; you verify with your OHIO email ([offer terms](https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0170p/)).
- **You cannot overspend by accident.** When the credit runs out the subscription is disabled, not billed, unless you upgrade to pay-as-you-go.
- **AI models are listed but not guaranteed.** Microsoft names Azure OpenAI and Microsoft Foundry among the included products ([Azure for Students](https://azure.microsoft.com/en-us/free/students/)), but does not publish which models a student subscription may deploy or its quota. Check in the Foundry portal before you design around one.
- **Choose a small model** ("mini" or "nano" class), which costs well under a cent per answer, and set a budget alert.
- **Best for** a project that must run off campus or on a public website.

### Gemini API free tier

- **Get a key** in [Google AI Studio](https://aistudio.google.com); you must be 18 or older ([terms](https://aistudio.google.com/docs/terms)).
- **Public or made-up data only.** Free-tier prompts are used to improve Google products and may be read by human reviewers; Google says not to send sensitive, confidential or personal information.
- **Limits are per project** and shown in AI Studio; daily limits reset at midnight Pacific ([rate limits](https://aistudio.google.com/docs/rate-limits)). Only some models are free ([pricing](https://aistudio.google.com/docs/pricing)).
- **It speaks the OpenAI API** (in beta), so the sample code below works with it ([OpenAI compatibility](https://aistudio.google.com/docs/openai)).

## Building the project

Write your code against the OpenAI Chat Completions API and keep three settings outside the code: base URL, API key and model. Every option with an API in this guide then becomes a settings change, not a rewrite.

| Where | `AI_BASE_URL` | `AI_MODEL` (example) | `AI_API_KEY` |
| --- | --- | --- | --- |
| AI-01 | http://ai-01.its.ohio.edu/api | gemma4:26b | Your AI-01 key |
| Gemini free tier | https://generativelanguage.googleapis.com/v1beta/openai/ | A free-tier model from AI Studio | Your AI Studio key |
| Azure for Students | https://YOUR-RESOURCE.openai.azure.com/openai/v1 | Your deployment's name | Key from the Azure portal |

Test a key before writing code: `curl http://ai-01.its.ohio.edu/api/models -H "Authorization: Bearer YOUR_KEY"` lists the models you can use (type `curl.exe` in Windows PowerShell).

### Settings file

Put the settings in a `.env` file next to your code, and add `.env` to `.gitignore` before your first commit.

```
AI_BASE_URL=http://ai-01.its.ohio.edu/api
AI_API_KEY=paste-your-key-here
AI_MODEL=gemma4:26b
```

### Sample code (Python)

Install the two libraries with `pip install openai python-dotenv`.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env from this folder

client = OpenAI(
    base_url=os.environ["AI_BASE_URL"],
    api_key=os.environ["AI_API_KEY"],
    timeout=180,  # campus servers can be slow when busy
)

reply = client.chat.completions.create(
    model=os.environ["AI_MODEL"],
    messages=[
        {"role": "system", "content": "You explain campus network services in plain language."},
        {"role": "user", "content": "What does DNS do, in two sentences?"},
    ],
)

print(reply.choices[0].message.content)
```

JavaScript, C# and most other languages have an OpenAI-compatible library that takes the same three settings.

### Habits that save you on demo day

- **Stream long answers** (`stream=True`) so users see text as it arrives.
- **Catch timeouts and errors.** Show a friendly message, retry once, then fall back to a second option from the table.
- **Send a short history:** the system prompt plus the last few turns, not the whole chat.
- **Log which model answered and how long it took.** Your write-up will need those numbers.
- **Need document search (embeddings)?** In the chat site, build a knowledge collection from your files under Workspace. Student API keys reach only gemma4:26b, so ask the admin before planning search in your own code.

## Choosing a path

Most projects fit AI-01; the rows below cover the exceptions.

| If your project | Use | Why |
| --- | --- | --- |
| Is a chatbot, assistant or summarizer demoed on campus | AI-01, gemma4:26b | Free default model, data stays on campus |
| Reads images or screenshots | AI-01, gemma4:26b | The default model reads images |
| Generates or explains code inside the app | AI-01, gemma4:26b | The only student model; fine for short code |
| Must work off campus or on a public website | Azure for Students, or Gemini free tier with public data only | AI-01 is campus only |
| Only needs AI while you plan, write or debug | Copilot Chat and GitHub Copilot Student | No API needed |

## Before you start

Work through these in order.

- [ ] Write one paragraph on what the AI does in your project and what data it will see.
- [ ] Confirm that data is public, low impact or made up.
- [ ] Check with your instructor how AI use will be graded and credited.
- [ ] Open the AI-01 Ollama/Open WebUI tile in Izzy and check that gemma4:26b is listed.
- [ ] Create an API key, put it in `.env`, and add `.env` to `.gitignore`.
- [ ] Run the sample code on campus and get an answer back.
- [ ] Set up a cloud fallback and test the switch.
- [ ] Keep a list of every AI tool you used, for your write-up.

Questions about access or the server go to your instructor or the server admin. Sensitive data sent to an AI by mistake goes to security@ohio.edu or 740-566-7233.

## Sources

Pages read on 2026-11-23:

- [OHIO: Secure Use of AI Tools standard](https://www.ohio.edu/oit/security/policy-practices/consulting/standards/secure-use-artificial-intelligence-tools)
- [OHIO: AI cybersecurity awareness guidance](https://www.ohio.edu/oit/security/ai-cybersecurity-awareness-guidance)
- [OHIO news: Microsoft Copilot now running GPT-5](https://www.ohio.edu/news/2025/10/microsoft-copilot-now-running-gpt-5)
- [GitHub Docs: Copilot for students](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)
- [GitHub: Copilot Student plan updates](https://github.com/orgs/community/discussions/189268)
- [GitHub Student Developer Pack](https://education.github.com/pack)
- [Azure for Students](https://azure.microsoft.com/en-us/free/students/) and its [offer terms](https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0170p/)
- [Gemini API pricing](https://aistudio.google.com/docs/pricing), [rate limits](https://aistudio.google.com/docs/rate-limits), [OpenAI compatibility](https://aistudio.google.com/docs/openai) and [terms](https://aistudio.google.com/docs/terms)

Server details come from the ECT server records as of November 2026.

# ECT AI Access: Azure

## Goals

- Find your own Azure AI key and endpoint
- Call GPT and Claude models from Python in VS Code on your gHost
- Keep your key secret and your usage reasonable

## Resources

- Your gHost (Ubuntu 24.04) with Visual Studio Code
- OHIO account
- An Azure AI resource that ECT created for you

## Environmental Context

- Your gHost on the ECT lab network, reached through Guacamole
- The models run in Microsoft Azure; your key works from any internet connection, which is why it must stay secret

## At a glance

This is the Azure option for the [ECT AI Access](Task-ECT-AI-Access.md) guide. When your course calls for it, ECT gives you your own Azure AI resource with GPT and Claude models. Nobody else uses your key, and your usage is recorded under your name.

How it compares with the other options:

- **Unlike AI-01**, it works off campus and answers in seconds.
- **Unlike Azure for Students**, ECT pays and sets it up; you do not need your own Azure subscription or credit.
- **Like every option**, it takes public, low impact or made-up data only.

| What | Yours |
| --- | --- |
| Resource name | Your course and NetID, for example `its2801-ab123456`; your welcome email has the exact name |
| Models | Listed in your welcome email; ITS 2801 gets `gpt-5.4-nano`, `gpt-5.4-mini` and `claude-haiku-5-5` |
| Limit per model | 20,000 tokens and 20 requests per minute |
| Key | Two keys, Key 1 and Key 2; you can see and regenerate both |
| Your usage | Visible to you in the Azure portal and to ECT staff |
| Access ends | The date in your welcome email (the end of the semester) |

## Ground rules

The full list is in [ECT AI Access](Task-ECT-AI-Access.md#ground-rules). The ones that matter most here:

- **Keep your key secret.** Not in your code, screenshots, chat, Canvas submissions or Git. It goes in a `.env` file that Git ignores.
- **Leaked a key? Regenerate it** (steps below). The old one stops working right away.
- **Public, low impact or made-up data only.** No student records, grades, passwords or anyone's personal information.
- **No endless loops or load tests.** Every call is billed to ECT and recorded under your name.
- **Use AI in coursework only as your instructor allows.**

## Getting access

1. Ask your instructor for Azure AI access. ECT creates your resource and emails you its name, a link and the endpoints.
2. Your resource works as soon as the email arrives. Nothing else needs to be installed or approved.

## Find your key

Open the Azure portal in your gHost's web browser, so you can copy the key and paste it inside the VM.

1. Open the link from your welcome email, or go to https://portal.azure.com and search for your resource name.
2. Sign in with your OHIO account.
3. In the menu on the left, open **Resource Management > Keys and Endpoint**.
4. Click **Show Keys**, then the copy icon beside **KEY 1**. If the page shows an error such as "Failed to list keys", Azure is having a problem; try again later.

To regenerate a key, click **Regenerate Key 1** on the same page. Update your `.env` file afterwards, because the old key stops working.

To see your own usage, open **Monitoring > Metrics**, pick **Input Tokens**, **Output Tokens** or **Model Requests** in the **Metric** box and **Sum** under **Aggregation**. Hover over the chart to read a value. For daily totals, click the time range at the top right and set **Time granularity** to **1 day**.

## Set up a project in VS Code

1. In the Terminal, make a folder for the project and a Python virtual environment inside it:

```
cd ~/python
mkdir ai-test
cd ai-test
python3 -m venv .venv
source .venv/bin/activate
pip install openai anthropic python-dotenv
code .
```

If `python3 -m venv` says that ensurepip is not available, run `sudo apt install python3-venv` and try again.

2. In VS Code, open the Command Palette (CONTROL-SHIFT-P), choose **Python: Select Interpreter** and pick the one in `.venv`.
3. Make a file named `.gitignore` with these two lines, before you make any commit:

```
.env
.venv/
```

4. Make a file named `.env` with your settings. Replace `its2801-ab123456` with the resource name from your welcome email and paste your key:

```
AI_BASE_URL=https://its2801-ab123456.openai.azure.com/openai/v1
AI_API_KEY=paste-your-key-here
AI_MODEL=gpt-5.4-mini
AZURE_RESOURCE=its2801-ab123456
```

## Call a GPT model

GPT models use the OpenAI API. Save this as `gpt_hello.py`:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env from this folder

client = OpenAI(
    base_url=os.environ["AI_BASE_URL"],
    api_key=os.environ["AI_API_KEY"],
    max_retries=5,  # retry brief network errors
)

reply = client.chat.completions.create(
    model=os.environ["AI_MODEL"],
    messages=[
        {"role": "system", "content": "You explain Python to beginners in plain language."},
        {"role": "user", "content": "What does a for loop do, in two sentences?"},
    ],
)

print(reply.choices[0].message.content)
print(f"[{reply.model}] tokens in/out: {reply.usage.prompt_tokens}/{reply.usage.completion_tokens}")
```

Run it in the Terminal with `python gpt_hello.py`. To try the other GPT model, change `AI_MODEL` in `.env` to `gpt-5.4-nano`.

## Call Claude

Claude uses the Anthropic API, through the `AnthropicFoundry` client for Azure. Save this as `claude_hello.py`:

```python
import os
from dotenv import load_dotenv
from anthropic import AnthropicFoundry

load_dotenv()

client = AnthropicFoundry(
    api_key=os.environ["AI_API_KEY"],
    resource=os.environ["AZURE_RESOURCE"],
    max_retries=5,
)

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=16000,
    system="You explain Python to beginners in plain language.",
    messages=[{"role": "user", "content": "What does a for loop do, in two sentences?"}],
)

if message.stop_reason == "refusal":
    print("The model declined this request.")
else:
    for block in message.content:
        if block.type == "text":
            print(block.text)
print(f"[{message.model}] tokens in/out: {message.usage.input_tokens}/{message.usage.output_tokens}")
```

Run it with `python claude_hello.py`. The same key works for both APIs.

## Which model to use

| Model | API | Use it for |
| --- | --- | --- |
| `gpt-5.4-nano` | OpenAI | The cheapest; short, simple tasks and quick tests |
| `gpt-5.4-mini` | OpenAI | Better answers, still inexpensive; a good default |
| `claude-haiku-5-5` | Anthropic | Claude's fast model; compare its answers with GPT's |

Both APIs send a list of messages and get text back, but the shapes differ: OpenAI puts the system prompt in the message list and returns `choices`, while Anthropic takes `system` separately, requires `max_tokens` and returns a list of content blocks.

## When something goes wrong

| You see | It means | Do this |
| --- | --- | --- |
| `401` or `Access denied due to invalid subscription key` | Wrong or regenerated key, or your access has ended | Copy KEY 1 again from the portal |
| `404` and `The API deployment for this resource does not exist` | The model name is misspelled or is not one of your three | Check the model name |
| `429` | Over 20 requests or 20,000 tokens a minute on that model | Wait a minute; add a pause between calls in loops |
| `Connection error` | A brief network problem | Run it again; `max_retries=5` already retries a few times |
| `KeyError: 'AI_API_KEY'` | Python did not find your `.env` | Run the script from the folder that holds `.env` |

## Habits that pay off

- **Print the token counts**, as the samples do. They show what each call costs and help you keep prompts short.
- **Send a short history:** the system prompt plus the last few turns, not a whole conversation.
- **Never commit `.env`.** Run `git status` before each commit; `.env` should not be listed.
- **Save your code to GitHub.** Your Azure resource is deleted after the semester; your code is yours to keep.

## Before you start

- [ ] Your welcome email from ECT has arrived.
- [ ] You can open your resource in the Azure portal and copy KEY 1.
- [ ] Your project has `.gitignore` (with `.env` and `.venv/`) and `.env`.
- [ ] `python gpt_hello.py` and `python claude_hello.py` both print an answer.

Questions about access go to your instructor or the ECT server admin. Sensitive data sent to an AI by mistake goes to security@ohio.edu or 740-566-7233.

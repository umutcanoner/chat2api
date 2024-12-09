# CHAT2API

🤖 A Simple ChatGPT TO API Proxy

🌟 Free and unlimited `GPT-3.5` without requiring an account

💥 Supports account usage with AccessToken, supports `O1-Preview/mini`, `GPT-4`, `GPT-4o/mini`, `GPTs`

🔍 Response format identical to the real API, compatible with almost all clients

👮 Companion user management system [Chat-Share](https://github.com/h88782481/Chat-Share) requires environment variables to be configured before use (ENABLE_GATEWAY set to True, AUTO_SEED set to False)

## Discussion Group

[https://t.me/chat2api](https://t.me/chat2api)

Before asking questions, please read the repository documentation thoroughly, especially the FAQ section.

When asking questions, please provide:

1. Startup log screenshots (sensitive information masked, including environment variables and version numbers)
2. Error log information (sensitive information masked)
3. Interface status codes and response bodies

## Sponsor

Thanks to Capsolver for sponsoring this project. For any CAPTCHA challenges, you can use [Capsolver](https://www.capsolver.com/zh?utm_source=github&utm_medium=repo&utm_campaign=scraping&utm_term=chat2api) to solve them

[![Capsolver](docs/capsolver.png)](https://www.capsolver.com/zh?utm_source=github&utm_medium=repo&utm_campaign=scraping&utm_term=chat2api)

## Features

### Latest version number is stored in `version.txt`

### Reverse API Features
> - [x] Streaming and non-streaming transmission
> - [x] No-login GPT-3.5 conversation
> - [x] GPT-3.5 model conversation (when model name doesn't include gpt-4, defaults to gpt-3.5, i.e., text-davinci-002-render-sha)
> - [x] GPT-4 series model conversation (include: gpt-4, gpt-4o, gpt-4o-mini, gpt-4-moblie in model name to use corresponding model, requires AccessToken)
> - [x] O1 series model conversation (include o1-preview, o1-mini in model name to use corresponding model, requires AccessToken)
> - [x] GPT-4 model drawing, coding, web browsing
> - [x] Supports GPTs (model name: gpt-4-gizmo-g-*)
> - [x] Supports Team Plus accounts (requires team account id)
> - [x] Upload images, files (in API corresponding format, supports URL and base64)
> - [x] Can be used as a gateway, supports distributed deployment
> - [x] Multi-account polling, supports both `AccessToken` and `RefreshToken`
> - [x] Request failure retry, automatically polls next Token
> - [x] Tokens management, supports uploading, clearing
> - [x] Scheduled refresh of `AccessToken` using `RefreshToken` / All non-forced refresh at startup, forced refresh every 4 days at 3 AM
> - [x] Supports file download, requires history recording enabled
> - [x] Supports `O1-Preview/mini` model inference process output

### Official Website Mirror Features
> - [x] Supports official website native mirroring
> - [x] Backend account pool random selection, `Seed` sets random account
> - [x] Direct login using `RefreshToken` or `AccessToken`
> - [x] Supports O1-Preview/mini, GPT-4, GPT-4o/mini
> - [x] Sensitive information API disabled, certain setting APIs disabled
> - [x] /login login page, automatic redirect to login page after logout
> - [x] /?token=xxx direct login, xxx is `RefreshToken` or `AccessToken` or `SeedToken` (random seed)

> TODO
> - [ ] Mirror support for `GPTs`
> - [ ] None currently, welcome to raise `issues`

## Reverse API

Completely `OpenAI` format API, supports passing `AccessToken` or `RefreshToken`, can use GPT-4, GPT-4o, GPTs, O1-Preview, O1-Mini:

```bash
curl --location 'http://127.0.0.1:5005/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Token}}' \
--data '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "stream": true
   }'
```

Pass your account's `AccessToken` or `RefreshToken` as `{{ Token }}`.
You can also fill in the value of environment variable `Authorization` you set, which will randomly select a backend account

For team accounts, you can pass `ChatGPT-Account-ID` to use Team workspace:

- Method 1:
Pass `ChatGPT-Account-ID` value in `headers`

- Method 2:
`Authorization: Bearer <AccessToken or RefreshToken>,<ChatGPT-Account-ID>`

If you've set the `AUTHORIZATION` environment variable, you can pass the set value as `{{ Token }}` for multi-Token polling.

> - `AccessToken` acquisition: After logging into ChatGPT official website, open [https://chatgpt.com/api/auth/session](https://chatgpt.com/api/auth/session) to get the `accessToken` value.
> - `RefreshToken` acquisition: Method not provided here.
> - No-login gpt-3.5 doesn't require Token.

## Tokens Management

1. Configure environment variable `AUTHORIZATION` as `authorization code`, then run the program.

2. Visit `/tokens` or `/{api_prefix}/tokens` to view existing Tokens count, upload new Tokens, or clear Tokens.

3. Pass the `authorization code` configured in `AUTHORIZATION` when making requests to use polling Tokens for conversation

![tokens.png](docs/tokens.png)

## Official Website Native Mirror

1. Set environment variable `ENABLE_GATEWAY` to `true`, then run the program. Note that after enabling, others can directly access your gateway through the domain name.

2. Upload `RefreshToken` or `AccessToken` on the Tokens management page

3. Visit `/login` to access the login page

![login.png](docs/login.png)

4. Enter the official website native mirror page to use

![chatgpt.png](docs/chatgpt.png)

## Environment Variables

Each environment variable has a default value. If you don't understand the meaning of environment variables, please don't set them, and especially don't pass empty values. Strings don't need quotes.

| Category | Variable Name | Example Value | Default Value | Description |
|----------|---------------|---------------|---------------|-------------|
| Security | API_PREFIX | `your_prefix` | `None` | API prefix password, easy to be accessed without setting, requires `/your_prefix/v1/chat/completions` after setting |
| | AUTHORIZATION | `your_first_authorization`,<br/>`your_second_authorization` | `[]` | Authorization code you set for using multi-account Token polling, separated by English commas |
| | AUTH_KEY | `your_auth_key` | `None` | Set this item if private gateway needs `auth_key` request header |
| Request | CHATGPT_BASE_URL | `https://chatgpt.com` | `https://chatgpt.com` | ChatGPT gateway address, changes request website when set, multiple gateways separated by commas |
| | PROXY_URL | `http://ip:port`,<br/>`http://username:password@ip:port` | `[]` | Global proxy URL, enable when getting 403, multiple proxies separated by commas |
| | EXPORT_PROXY_URL | `http://ip:port` or<br/>`http://username:password@ip:port` | `None` | Export proxy URL, prevents source IP leakage when requesting images and files |
| Features | HISTORY_DISABLED | `true` | `true` | Whether to not save chat history and return conversation_id |
| | POW_DIFFICULTY | `00003a` | `00003a` | Proof of work difficulty to solve, don't set if you don't understand |
| | RETRY_TIMES | `3` | `3` | Error retry count, automatically random/polls next account when using `AUTHORIZATION` |
| | CONVERSATION_ONLY | `false` | `false` | Whether to use conversation interface directly, enable only if your gateway supports automatic POW solving |
| | ENABLE_LIMIT | `true` | `true` | When enabled, doesn't attempt to break official count limits, helps prevent account bans |
| | UPLOAD_BY_URL | `false` | `false` | When enabled, conversation follows `URL+space+content` format, automatically parses and uploads URL content, multiple URLs separated by spaces |
| | SCHEDULED_REFRESH | `false` | `false` | Whether to refresh `AccessToken` on schedule, when enabled will non-forcefully refresh all at startup, forcefully refresh all every 4 days at 3 AM |
| | RANDOM_TOKEN | `true` | `true` | Whether to randomly select backend `Token`, enables random backend account when on, sequential polling when off |
| Gateway | ENABLE_GATEWAY | `false` | `false` | Whether to enable gateway mode, can use mirror site when enabled but will be unprotected |
| | AUTO_SEED | `false` | `true` | Whether to enable random account mode, enabled by default, randomly matches backend `Token` after entering `seed`. When disabled, requires manual interface connection for `Token` control |

## Deployment

### Zeabur Deployment

[![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/templates/6HEGIZ?referralCode=LanQian528)

### Direct Deployment

```bash
git clone https://github.com/LanQian528/chat2api
cd chat2api
pip install -r requirements.txt
python app.py
```

### Docker Deployment

You need to install Docker and Docker Compose.

```bash
docker run -d \
  --name chat2api \
  -p 5005:5005 \
  lanqian528/chat2api:latest
```

### (Recommended, PLUS account usable) Docker Compose Deployment

Create a new directory, e.g., chat2api, and enter it:

```bash
mkdir chat2api
cd chat2api
```

Download the docker-compose.yml file from the repository in this directory:

```bash
wget https://raw.githubusercontent.com/LanQian528/chat2api/main/docker-compose-warp.yml
```

Modify environment variables in docker-compose-warp.yml file, then save and:

```bash
docker-compose up -d
```

## FAQ

> - Error codes:
>   - `401`: Current IP doesn't support no-login, try changing IP address, or set proxy in environment variable `PROXY_URL`, or your authentication failed.
>   - `403`: Check specific error message in logs.
>   - `429`: Current IP exceeded request limit within 1 hour, please try again later or change IP.
>   - `500`: Internal server error, request failed.
>   - `502`: Server gateway error or network unavailable, try changing network environment.

> - Known situations:
>   - Many Japanese IPs don't support no-login, US IPs recommended for no-login GPT-3.5.
>   - 99% of accounts support free `GPT-4o`, but activation depends on IP region, currently Japan and Singapore IPs known to have higher activation probability.

> - What is environment variable `AUTHORIZATION`?
>   - It's a self-set authentication for chat2api, required for using saved Tokens polling, pass it as `APIKEY` when making requests.
> - How to get AccessToken?
>   - After logging into ChatGPT official website, open [https://chatgpt.com/api/auth/session](https://chatgpt.com/api/auth/session) to get the `accessToken` value.

## License

MIT License

# Technical Test Part 1 - Written Answers

---

## ChatGPT and Claude

### 1. System instruction vs. user message
A system instruction sets the overall role, tone, and permanent rules for the AI, while a user message contains the specific question or task for that particular request.

Any rule that must apply to every single request should be placed in the system instruction rather than repeating it in user messages. Keeping global rules there ensures they are followed consistently and stay protected if a user input tries to override them.

---

### 2. Valid JSON vs. JSON schema validation
Valid JSON only means the text is formatted properly with correct brackets, quotes, and commas, whereas matching a JSON schema means the data also has the exact fields, structure, and data types our system expects.

An automation should always validate the AI output against a schema before using it because even valid JSON can miss a required key or have a string where a number is needed. Checking the schema early catches bad outputs right away and stops the next workflow steps or API calls from failing.

---

### 3. Non-determinism and routing decisions
ChatGPT and Claude do not always give the exact same wording for the same prompt because they generate replies based on probability and settings like temperature.

If an AI reply directly controls a routing decision, even a small change in phrasing can fail an exact-match check and send a customer or record to the wrong path. To avoid this, we should use low temperature, restrict the output to fixed options using a schema, and keep a fallback branch ready.

---

### 4. Prompt injection and untrusted input
Prompt injection happens when someone hides instructions inside a message or document to trick the AI into ignoring its original rules.

Customer messages and fetched documents should always be treated as untrusted input because someone can put sneaky commands inside an email, chat, or knowledge base file to change the output or pull out private details. Keeping system rules separate from user data, validating outputs, and limiting what tools the AI can run helps keep the workflow safe.

---

## GoHighLevel (GHL) and Integrations

### 5. Trigger, action, and If/Else branch
A trigger is the starting event that puts a contact into a GoHighLevel workflow, such as submitting a form or getting a new tag.

An action is the actual task the workflow carries out, like sending an SMS, updating a contact detail, or calling a webhook. An If/Else branch checks conditions on the contact or event data so the workflow can take different paths based on the result.

---

### 6. Webhooks vs. polling
A webhook is an automatic HTTP message that one app sends to another app's URL as soon as an event takes place.

Unlike polling-where an automation keeps calling an API again and again on a timer to check for updates-a webhook pushes the update immediately only when something actually happens. This saves unnecessary API calls, avoids hitting rate limits, and removes waiting delays.

---

### 7. Idempotency and duplicate webhooks
Idempotency means running the same step once or multiple times with the same input gives the exact same final result without creating duplicates.

Webhook providers often resend the same event if there is a network timeout or temporary error, so our automation can receive the same webhook more than once. Making our handler idempotent-for example, by saving and checking the event ID-prevents sending duplicate messages, double-updating CRM records, or repeating actions.

---

### 8. Temporary API timeout vs. missing required field
A temporary API timeout is a short-term network or server issue that can be retried after a brief wait, whereas a request rejected for a missing required field is a data error that will fail every time if retried as-is.

Instead of retrying a missing-field error and wasting API calls, the automation should log the issue and notify the team or send the record for correction. Retries only make sense for temporary problems like timeouts, rate limits (HTTP 429), or brief server errors (HTTP 5xx), where trying again after a short backoff has a good chance of working.

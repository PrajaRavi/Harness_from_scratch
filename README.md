# Groq Python SDK Error Reference

This document outlines the exception classes provided by the Groq SDK and what each one represents during an API call.

## Base Exceptions
- **`GroqError`**: The base exception class for all errors raised by the Groq SDK. Catching this allows you to handle any Groq-specific exception broadly.
- **`APIError`**: A general error class representing issues returned by the API layer.

## Connection & Timing Exceptions
- **`APIConnectionError`**: Raised when the client fails to establish a network connection with the Groq API (e.g., DNS resolution failure, network offline, or dropped connection).
- **`APITimeoutError`**: Raised when a request takes longer than the configured timeout threshold to receive a response from the server.

## Status & HTTP Client Errors (4xx)
- **`APIStatusError`**: Base class for any response that returns a non-2xx HTTP status code.
- **`BadRequestError`** (HTTP 400): The request was malformed, missing required fields, or contained invalid syntax.
- **`AuthenticationError`** (HTTP 401): The API key provided is missing, expired, or invalid.
- **`PermissionDeniedError`** (HTTP 403): Your account or API key does not have the necessary permissions to access the requested resource or model.
- **`NotFoundError`** (HTTP 404): The requested resource or endpoint does not exist (commonly thrown if you pass an incorrect or deprecated model name).
- **`UnprocessableEntityError`** (HTTP 422): The request was syntactically correct, but the semantic parameters provided could not be processed by the model or server.
- **`RateLimitError`** (HTTP 429): You have exceeded your rate limits (requests per minute or tokens per minute) or run out of quota.

## Server Errors (5xx)
- **`InternalServerError`** (HTTP 500): Groq's internal servers encountered an unexpected condition or failure while processing your request.
```text
future improvement->implement robust error handelling
```
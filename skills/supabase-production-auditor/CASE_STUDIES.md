# Case studies

Developed by the LetsCookTech Open Source Team.

## SaaS workspace app

Expected catches: organization membership checks, tenant-scoped RLS, invitation abuse, service-role boundaries, and billing metadata exposure.

## AI application

Expected catches: chat history privacy, embedding storage, vector search leakage, prompt storage, model-cost abuse, and RAG document access control.

## Mobile app

Expected catches: anonymous access, weak storage policies, client-side trust assumptions, and missing rate limits.

## Security breach example

A policy allows authenticated users to read all rows because it checks login state but not tenant membership. The auditor should mark this as critical.

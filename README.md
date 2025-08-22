# 🛠️ AWS Lambda CI/CD Automation with GitHub Actions

This project demonstrates a **minimal but complete CI/CD pipeline** for deploying a Python AWS Lambda function. It includes unit testing, linting, and fully automated deployment to AWS using GitHub Actions.

## 📌 Project Overview

The Lambda function retrieves exchange rates from an external API and stores the data (USD→TWD, HKD→TWD) into a DynamoDB table.

### 🔧 Tech Stack

- **Python 3.11** + `pytest`, `flake8`
- **AWS Lambda** + **DynamoDB**
- **GitHub Actions** for CI/CD automation
- **IAM & Secrets** for secure AWS credential management

---

## ✅ What’s Included

| Stage | Feature |
|-------|---------|
| 🧪 CI - Testing | Unit tests with `pytest`, mocks for API & DB |
| 🧹 CI - Linting | Code style enforcement via `flake8` |
| 🔑 Secure Deployment | IAM user + GitHub Secrets for AWS access |
| 🚀 CD - Deployment | Automatic zip packaging and `aws lambda update-function-code` |
| 🧾 Error Handling | Full error trace review and recovery from DynamoDB & API issues |

---

## 🧑‍💼 Why It Matters for Tech PM / PO Role

As a transitioning **Technical Project Manager / Product Owner**, this project highlights:

- ✅ Hands-on experience building **production-grade DevOps pipelines**
- ✅ Understanding of **developer workflows** and how to automate them
- ✅ Ability to **collaborate with developers** using real tooling
- ✅ Experience troubleshooting **CI failures** and AWS permission errors
- ✅ Communication of **technical risks and constraints** to stakeholders

---

## 📷 Demo

![CI/CD Flow](https://github.com/susancat/exchangerate/actions) *(optional)*

---

## 🧩 Next Steps

- Add test coverage reports
- Enable multi-environment deployment
- Convert to SAM / Serverless framework for scalability

---

## 🔗 Related

- [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

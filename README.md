# Building-a-Proof-of-Concept-for-a-Serverless-Solution

Building a Proof of Concept for a Serverless Solution

Overview
This project demonstrates a serverless architecture on AWS designed to handle scalable and decoupled web backend operations for an e-commerce platform selling cleaning supplies. The solution leverages AWS services like API Gateway, SQS, Lambda, DynamoDB, and SNS to ensure scalability, reliability, and real-time notifications.

 Architecture
The architecture follows an event-driven workflow:

API Gateway receives REST API requests and forwards them to Amazon SQS.

SQS triggers Lambda (POC-Lambda-1) to insert records into DynamoDB.

DynamoDB Streams captures changes and invokes a second Lambda (POC-Lambda-2).

Lambda-2 publishes the record to Amazon SNS, sending email notifications to subscribers.

 AWS Services Used
API Gateway: REST API endpoint for client interactions.

SQS: Decouples API Gateway from Lambda, ensuring message durability.

Lambda: Serverless compute for processing data (Python 3.9).

DynamoDB: NoSQL database with streams for real-time change capture.

SNS: Pub/sub service for email notifications.

IAM: Role-based permissions for secure access.
 Key Steps Implemented
IAM Setup: Custom policies/roles for least-privilege access.

DynamoDB Table: Created orders table with orderID as the partition key.

SQS Queue: Configured with access policies for Lambda and API Gateway.

Lambda Functions:

POC-Lambda-1: Processes SQS messages → DynamoDB.

POC-Lambda-2: Processes DynamoDB streams → SNS.

SNS Topic: Email subscription for order notifications.

API Gateway: POST method to push data to SQS.

Testing the Workflow
Send a mock order (e.g., {"item": "latex gloves", "customerID": "12345"}) via API Gateway.

Verify:

Data appears in DynamoDB.

Email notification received via SNS.

🧹 Cleanup Instructions
To avoid unnecessary AWS charges, delete all resources after testing:

bash
1. DynamoDB Table: `orders`  
2. Lambda Functions: `POC-Lambda-1`, `POC-Lambda-2`  
3. SQS Queue: `POC-Queue`  
4. SNS Topic: `POC-Topic` and its subscription  
5. API Gateway: `POC-API`  
6. IAM Roles/Policies: Listed in Task 10 of the PDF.  
📄 Documentation
Full step-by-step guide: Architecting Solutions.pdf

Architecture diagram: Schema d'archiecture.png

💡 Learning Outcomes
Designed a scalable serverless backend for fluctuating workloads.

Implemented event-driven workflows using AWS services.

Practiced AWS best practices (IAM roles, decoupled components).

🔗 GitHub Repo: (https://github.com/galileekamdem/Building-a-Proof-of-Concept-for-a-Serverless-Solution)
👨‍💻 Author: Kevin M. KAMDEM
📅 Date: 09/07/2025

🌟 Star this repo if you found it useful! Contributions and feedback are welcome.

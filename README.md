# Elastic Search Flask App

This project demonstrates how to integrate Elasticsearch with a Flask web application. It includes a dynamic search interface built with Tailwind CSS and a Python script to ingest data from a CSV file into Elasticsearch.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Running Elasticsearch with Docker](#1-running-elasticsearch-with-docker)
  - [2. Setting Up the Flask App](#2-setting-up-the-flask-app)
  - [3. Ingesting Data into Elasticsearch](#3-ingesting-data-into-elasticsearch)
  - [4. Running the Flask App](#4-running-the-flask-app)
  - [5. Using the Search Interface](#5-using-the-search-interface)
- [Project Structure](#project-structure)
- [Additional Notes](#additional-notes)
- [License](#license)

## Overview

This project provides a complete setup that:
- Runs an Elasticsearch instance via Docker.
- Ingests a publicly available large dataset (CSV file) into Elasticsearch.
- Implements a Flask app with a dynamic search interface that queries Elasticsearch using a prefix-based search.
- Implement search UI with TailwindCSS.

## Prerequisites

- [Docker](https://www.docker.com/) (to run Elasticsearch)
- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

## Getting Started

### 1. Running Elasticsearch with Docker

Pull the Elasticsearch Docker image and run a single-node cluster on port 9200:

```bash
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.9
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.9
```
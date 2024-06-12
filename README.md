
# CS50 Wiki

Welcome to the CS50 Wiki project! This is a web-based application developed as part of Harvard's CS50's Web Programming with Python and JavaScript course. The Wiki project is a simple yet functional encyclopedia where users can create, edit, and view pages using Markdown syntax.


## Features

- **Markdown Support:** Write content using Markdown, which will be rendered as HTML.
- **Create New Pages:** Easily add new pages to the wiki.
- **Edit Existing Pages:** Modify the content of existing pages.
- **Search Functionality:** Search for pages by their title.
- **Random Page:** Get inspired by reading a random page from the wiki.


## Project Structure

Here's the breakdown of the Project's structure:

```
CS50-Wiki/
├── encyclopedia/
│   ├── static/encyclopedia/
│   │   └── style.css
│   ├── templates/encyclopedia/
│   │   ├── edit.html
│   │   ├── error.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── new.html
│   │   └── entry.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── entries/
│   ├── ...
├── wiki/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```
## Getting Started

**Prerequisites**

- Python 3.8+
- Django 3.1+
- Git (for version control)

**Installation**
#### 1. Clone the repository:

```bash
git clone https://github.com/Master-Vasu/CS50-Wiki.git
cd CS50-Wiki
```

#### 2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

#### 3. Install dependencies:

```bash
pip install -r requirements.txt
``` 

#### 4. Apply migrations:

```bash
python manage.py migrate
``` 

#### 5. Run the surver:

```bash
python manage.py runserver
``` 

#### 6. Open your browser and visit `http://127.0.0.1:8000`.
## Usage

**Creating a new page:**

1. Navigate to the "Create New Page" section.

2. Enter the title of the page and write your content in Markdown.

3. Click "Save" to add the new page to the wiki.

**Editing a Page**

1. Open the page you want to edit.

2. Click the "Edit" button.

3. Modify the content and click "Save" to update the page.

**Searching for Pages**

- Use the search bar at the top to find pages by their title.

**Viewing a Random Page**

- Click on "Random Page" to explore a random entry from the wiki.

## Video Demo

YouTube Link: [Wiki Demo](https://youtu.be/gVNh3N6Tgl8?si=eVNIaLd_Vf4Dp9P2)


## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue with your suggestions. Please follow the guidelines below when contributing:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

## Acknowledgments

- [CS50 Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/) - The course that inspired this project.
- The amazing team and community at Harvard University and CS50.
- [Django](https://www.djangoproject.com/) - For the web framework.

## Contact

If you have any questions or feedback, feel free to reach out:

- GitHub: [Master-Vasu](https://github.com/Master-Vasu)
- Twitter/X: [Vasu_arcR](https://x.com/Vasu_arcR)
- vasumoradiya@gmail.com
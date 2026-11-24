#!/usr/bin/env python
"""Utilitário de linha de comando do Django (gerado pelo startproject)."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django não encontrado. Ativou a venv e rodou 'pip install django'?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

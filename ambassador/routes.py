from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from ambassador import app, db, bcrypt  # Adjust import based on your actual package structure
from ambassador.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, CommentForm
from ambassador.models import User, Post, Comment, Like  # Adjust import based on your actual package structure
from datetime import datetime
from flask import Blueprint

bp = Blueprint('home', __name__)








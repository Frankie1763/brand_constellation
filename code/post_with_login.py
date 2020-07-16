import instaloader
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--VM_RANK', type=int, default= 1,
                    help='Starting point.')
parser.add_argument('--VM_TOTAL', type=int, default= 1,
                    help='Crawling Step.')
parser.add_argument('--U', type=str, default='sophie_chowww',
                    help='Username.')
parser.add_argument('--P', type=str, default='990126',
                    help='Password.')

L = instaloader.Instaloader()

# Optionally, login or load session
L.login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file(USER) # (load session created w/
                               #  `instaloader -l USERNAME`)
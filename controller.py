import view
import model
import logger


def run():
    while True:
        mode = view.choice()
        if mode == '1':
            contact = view.contact_new()
            logger.new(contact)
        elif mode == '2':
            contact = view.contact_find()
            base = logger.old(contact)
            result = model.search(base, contact)
            view.find(result)

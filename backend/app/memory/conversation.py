conversation_history = [] 
#it breaks encapsulation

def add_user_message(message: str):

    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_assistant_message(message: str):

    conversation_history.append(
        {
            "role": "assistant",
            "content": message
        }
    )


def get_conversation():

    return conversation_history


def clear_conversation():

    conversation_history.clear()
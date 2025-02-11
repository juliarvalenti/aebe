import os
import pickle
import uuid

from dotenv import load_dotenv

load_dotenv()


def default_config():
    """Prepare the default configuration"""

    # TODO Turn these all into environment variables
    return {
        "max_steps": 100,
        "max_actions_per_step": 10,
        "use_vision": False,
        "tool_calling_method": "auto",
        "llm_provider": "openai",
        "llm_model_name": os.getenv("OPENAI_MODEL_NAME", "gpt-4o"),
        "llm_temperature": 1.0,
        "llm_base_url": os.getenv("OPENAI_ENDPOINT", "https://api.openai.com/v1"),
        "llm_api_key": os.getenv("OPENAI_API_KEY", ""),
        # "use_own_browser": os.getenv("CHROME_PERSISTENT_SESSION", "false").lower() == "true",
        # "keep_browser_open": False,
        "use_own_browser": False,
        "keep_browser_open": True,    
        "headless": False,
        "disable_security": True,
        "enable_recording": True,
        "window_w": 1280,
        "window_h": 1100,
        "save_recording_path": "./tmp/record_videos",
        "save_trace_path": "./tmp/traces",
        "save_agent_history_path": "./tmp/agent_history",
        "task": "go to google.com and type 'OpenAI' click search and give me the first url",
    }


def load_config_from_file(config_file):
    """Load settings from a UUID.pkl file."""
    try:
        with open(config_file, 'rb') as f:
            settings = pickle.load(f)
        return settings
    except Exception as e:
        return f"Error loading configuration: {str(e)}"


def save_config_to_file(settings, save_dir="./tmp/webui_settings"):
    """Save the current settings to a UUID.pkl file with a UUID name."""
    os.makedirs(save_dir, exist_ok=True)
    config_file = os.path.join(save_dir, f"{uuid.uuid4()}.pkl")
    with open(config_file, 'wb') as f:
        pickle.dump(settings, f)
    return f"Configuration saved to {config_file}"


def save_current_config(*args):
    current_config = {
        "agent_type": args[0],
        "max_steps": args[1],
        "max_actions_per_step": args[2],
        "use_vision": args[3],
        "tool_calling_method": args[4],
        "llm_provider": args[5],
        "llm_model_name": args[6],
        "llm_temperature": args[7],
        "llm_base_url": args[8],
        "llm_api_key": args[9],
        "use_own_browser": args[10],
        "keep_browser_open": args[11],
        "headless": args[12],
        "disable_security": args[13],
        "enable_recording": args[14],
        "window_w": args[15],
        "window_h": args[16],
        "save_recording_path": args[17],
        "save_trace_path": args[18],
        "save_agent_history_path": args[19],
        "task": args[20],
    }
    return save_config_to_file(current_config)

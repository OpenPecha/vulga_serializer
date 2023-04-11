def get_token_text(token_info):
    token_text = token_info['text'].replace("\n", "𰵁")
    return token_text

def is_best_version(version_info):
    if version_info['is_top_weight']:
        return True
    return False

def get_versions(token_entry):
    versions = {}
    best_version = ""
    for witness_id, version_info in token_entry.items():
        version_text = get_token_text(version_info)
        if is_best_version(version_info):
            best_version = version_text
        versions[witness_id] = version_text
    return versions, best_version

def has_diff(versions):
    version_texts = list(versions.values())
    unique_versions = set(version_texts)
    if len(unique_versions) > 1:
        return True
    return False

def is_punct_note(note):
    note = note.strip()
    if note in ["་", "།", "༔", ":", "། །", "༄", "༅", "\u0F7F", " ", "༑",]:
        return True
    else:
        return False
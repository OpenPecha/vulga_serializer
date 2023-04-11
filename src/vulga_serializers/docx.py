import re
from pypandoc import convert_text

from vulga_serializers.utils import get_versions, has_diff


def regroup_same_notes(note_options, witness_mapping):
    regrouped_notes = {}
    for pub, note_text in note_options.items():
        pub = witness_mapping.get(pub, pub)
        regrouped_notes[note_text] = [pub] if note_text not in regrouped_notes.keys() else regrouped_notes[note_text] + [pub]
    return regrouped_notes


def get_note_text(note_options, witness_mapping, best_version):
    note_text = f"{best_version}] "
    regrouped_notes = regroup_same_notes(note_options, witness_mapping)
    for note, pubs in regrouped_notes.items():
        pub_names = ','.join(pubs)
        note_text += f"{pub_names}: {note}; "
    return note_text[:-1]

def get_note_annotation(versions, note_walker, witness_mapping, best_version):
    
    note_annotation = f'[^{note_walker}]: {get_note_text(versions, witness_mapping, best_version)}\n'
    return note_annotation


def get_collated_text(vulga_report, output_dir, docx_file_name):
    collated_text = ""
    note_text = ""
    note_walker = 1
    witness_mapping = vulga_report['witness_mapping']
    vulga_report.pop('witness_mapping')
    for _, versions_entry in vulga_report.items():
        versions, best_version = get_versions(versions_entry)
        if has_diff(versions):
            note_text += get_note_annotation(versions, note_walker, witness_mapping, best_version)
            if best_version:
                collated_text += f'{best_version}[^{note_walker}]'
            else:
                collated_text += f'[^{note_walker}]'
            note_walker += 1
        else:
            collated_text += f'{best_version}'
    collated_text += f'\n\n{note_text}'
    collated_text_md = re.sub('𰵁', '\n', collated_text)
    output_path = output_dir / f"{docx_file_name}.docx"
    convert_text(
        collated_text_md, "docx", "markdown", outputfile=str(output_path)
    )
    return collated_text_md



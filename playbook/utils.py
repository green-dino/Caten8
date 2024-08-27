# utils.py
import json
import graphviz as gv
from pyvis.network import Network

class PlaybookUtils:
    @staticmethod
    def validate_input(play_name, roles, blocks, tasks):
        errors = []
        if not play_name:
            errors.append("Play name is required.")
        if not roles:
            errors.append("At least one role is required.")
        if not blocks:
            errors.append("At least one block is required.")
        if not tasks:
            errors.append("At least one task is required.")
        if any(not item for item in roles + blocks + tasks):
            errors.append("All entries must contain at least one item.")
        return errors

    @staticmethod
    def save_playbook_to_file(playbook_data, version, author, filename="playbook.json"):
        playbook_data.update({"version": version, "author": author})
        try:
            with open(filename, "w") as file:
                json.dump(playbook_data, file)
        except TypeError as e:
            raise Exception(f"Error saving playbook: {e}")

    @staticmethod
    def load_playbook_from_file(filename="playbook.json"):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            raise Exception(f"Error loading playbook: {e}")

class PlaybookGraphCreator:
    def __init__(self, play_name, roles, blocks, tasks):
        self.dot = gv.Digraph()
        with self.dot.subgraph(name='cluster_playbook') as playbook:
            playbook.attr(label='Playbook')
            playbook.node('Play', play_name)
            self._add_nodes(playbook, roles, 'Role')
            self._add_nodes(playbook, blocks, 'Block')
            self._add_nodes(playbook, tasks, 'Task')

    def _add_nodes(self, playbook, items, prefix):
        for item in items:
            node_id = f'{prefix}_{item}'
            playbook.node(node_id, item)
            playbook.edge('Play', node_id)

    def get_dot(self):
        return self.dot

class InteractiveGraphCreator:
    @staticmethod
    def create_interactive_graph(play_name, roles, blocks, tasks):
        net = Network(directed=True)
        net.add_node(play_name, label=play_name, color='red', size=25)
        InteractiveGraphCreator._add_nodes(net, roles, play_name, 'blue')
        InteractiveGraphCreator._add_nodes(net, blocks, play_name, 'green')
        InteractiveGraphCreator._add_nodes(net, tasks, play_name, 'orange')
        return net

    @staticmethod
    def _add_nodes(net, items, parent, color):
        for item in items:
            net.add_node(item, label=item, color=color)
            net.add_edge(parent, item)
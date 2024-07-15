# Outil de Surveillance Réseau

Ce script Python est conçu pour surveiller et analyser le trafic réseau sur une interface spécifiée. Il collecte des informations sur les paquets, les connexions, et les statistiques de transfert de données.

## Fonctionnalités

- **Surveillance du Réseau:** Capture les paquets sur une interface réseau spécifiée.
- **Statistiques de Trafic:** Calcule et affiche les statistiques de trafic réseau, y compris le nombre total de paquets et les connexions principales.
- **Informations sur les Connexions:** Affiche les cinq connexions les plus fréquentes.
- **Statistiques d'E/S:** Affiche les statistiques de transfert de données (octets envoyés et reçus).

## Prérequis

- Python 3.x
- Bibliothèque `psutil`
- Bibliothèque `scapy`

Vous pouvez installer les bibliothèques requises en utilisant pip :
```sh
pip install psutil scapy
```

## Utilisation

### Arguments de Ligne de Commande

- `-i` ou `--interface` : Spécifie l'interface réseau à surveiller (obligatoire).
- `-d` ou `--duration` : Spécifie la durée de la surveillance en secondes (optionnel, par défaut : 60 secondes).

### Exemple d'Exécution

Pour exécuter le script et surveiller l'interface `eth0` pendant 60 secondes, utilisez la commande suivante :

```sh
python network_monitor.py -i eth0 -d 60
```

### Liste des Interfaces Réseau

Si l'interface spécifiée n'est pas trouvée, le script affichera la liste des interfaces réseau disponibles.

## Code

```python
import argparse
import psutil
import time
from collections import defaultdict
from scapy.all import sniff, IP

class NetworkMonitor:
    def __init__(self):
        self.packet_counts = defaultdict(int)
        self.start_time = time.time()

    def packet_callback(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            self.packet_counts[(src_ip, dst_ip)] += 1

    def monitor_network(self, interface, duration):
        print(f"Monitoring network on {interface} for {duration} seconds...")
        sniff(iface=interface, prn=self.packet_callback, timeout=duration)

    def print_stats(self):
        print("\nNetwork Statistics:")
        total_packets = sum(self.packet_counts.values())
        elapsed_time = time.time() - self.start_time
        print(f"Total packets: {total_packets}")
        print(f"Packets per second: {total_packets / elapsed_time:.2f}")
        print("\nTop 5 connections:")
        for (src, dst), count in sorted(self.packet_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"{src} -> {dst}: {count} packets")

        io = psutil.net_io_counters()
        print(f"\nBytes sent: {io.bytes_sent}")
        print(f"Bytes received: {io.bytes_recv}")

def list_interfaces():
    interfaces = psutil.net_if_addrs()
    print("Available network interfaces:")
    for interface in interfaces:
        print(f" - {interface}")

def main():
    parser = argparse.ArgumentParser(description="Network Monitoring Tool")
    parser.add_argument('-i', '--interface', type=str, help='Network interface to monitor', required=True)
    parser.add_argument('-d', '--duration', type=int, help='Monitoring duration in seconds', default=60)
    args = parser.parse_args()

    if args.interface not in psutil.net_if_addrs():
        print(f"Error: Interface {args.interface} not found.")
        list_interfaces()
        return

    monitor = NetworkMonitor()
    monitor.monitor_network(args.interface, args.duration)
    monitor.print_stats()

if __name__ == "__main__":
    main()
```

## Avertissements

- Assurez-vous d'avoir les permissions nécessaires pour surveiller l'interface réseau spécifiée.
- L'utilisation de ce script peut nécessiter des privilèges d'administrateur/root, selon votre système d'exploitation et votre configuration réseau.

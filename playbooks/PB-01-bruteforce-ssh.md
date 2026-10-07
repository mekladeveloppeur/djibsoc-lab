# PB-01 — Brute force SSH

**Règles liées :** 100001, 100005 · **MITRE :** T1110, T1078 · **Sévérité :** Haute / Critique

## 1. Détection et qualification
- Récupérer l'alerte (IP source, utilisateur ciblé, nombre d'échecs, horodatage).
- Vérifier la réputation de l'IP (AbuseIPDB, VirusTotal).
- Y a-t-il une **connexion réussie** (règle 100005) depuis la même IP ? Si oui → **incident critique**, passer directement à l'étape 3.

## 2. Investigation
```bash
grep "Failed password" /var/log/auth.log | grep <IP> | tail -50
grep "Accepted" /var/log/auth.log | grep <IP>
```
- Lister les comptes ciblés (comptes valides ou inexistants ?).
- Rechercher d'autres alertes de la même IP sur d'autres hôtes.

## 3. Confinement
- Bloquer l'IP au pare-feu : `sudo ufw deny from <IP>`
- Si connexion réussie : verrouiller le compte (`sudo passwd -l <user>`), terminer les sessions (`sudo pkill -u <user>`), isoler la machine.

## 4. Éradication et récupération
- Réinitialiser les identifiants, désactiver l'authentification par mot de passe, activer les clés SSH.
- Vérifier la persistance : `crontab -l`, `~/.ssh/authorized_keys`, nouveaux comptes (voir PB-02).

## 5. Prévention
- Désactiver `PermitRootLogin`, installer `fail2ban`, restreindre SSH par IP/VPN, activer le MFA.

## 6. Clôture
Remplir le [rapport d'incident](../templates/rapport-incident.md).

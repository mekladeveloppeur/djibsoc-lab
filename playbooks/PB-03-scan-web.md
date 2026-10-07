# PB-03 — Scan / reconnaissance web

**Règle liée :** 100004 · **MITRE :** T1595 · **Sévérité :** Moyenne

## 1. Qualification
- Identifier l'IP, le user-agent et les URL demandées.
- Distinguer un scanner automatisé d'un test de sécurité planifié (vérifier le calendrier des pentests).

## 2. Investigation
```bash
grep <IP> /var/log/nginx/access.log | awk '{print $9}' | sort | uniq -c
```
- Des réponses `200` ou `500` indiquent une exposition potentielle : à analyser en priorité.

## 3. Confinement
- Bloquer l'IP ou la plage au niveau WAF / pare-feu.
- Activer la limitation de débit (rate limiting).

## 4. Amélioration
- Supprimer les pages inutiles exposées, mettre à jour l'application, vérifier la conformité OWASP Top 10.

## 5. Clôture
Rapport d'incident.

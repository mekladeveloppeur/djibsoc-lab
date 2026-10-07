# PB-02 — Création de compte suspecte

**Règle liée :** 100002 · **MITRE :** T1136.001 · **Sévérité :** Moyenne / Haute

## 1. Qualification
- Le compte a-t-il été créé dans le cadre d'un changement approuvé (ticket) ?
- Qui l'a créé (utilisateur, heure, session) ?

## 2. Investigation
```bash
grep "useradd\|new user" /var/log/auth.log
id <compte> ; last <compte> ; sudo -l -U <compte>
getent group sudo
```
- Vérifier les clés SSH (`/home/<compte>/.ssh/authorized_keys`) et les tâches cron.

## 3. Confinement
- Si non autorisé : `sudo usermod -L <compte>` puis `sudo pkill -u <compte>`.
- Conserver les preuves avant suppression (copie des journaux, du dossier home).

## 4. Éradication
- Supprimer le compte, auditer les autres comptes et les fichiers modifiés récemment.
- Identifier le vecteur d'accès initial (voir PB-01).

## 5. Clôture
Rapport d'incident + mise à jour de la procédure de gestion des accès (ISO 27001 A.5.15 / A.5.18).

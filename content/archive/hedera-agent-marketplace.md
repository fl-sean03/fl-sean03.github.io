---
title: "Hedera Agent Marketplace"
description: "On-chain registry and settlement layer for autonomous agents"
date: 2026-02-01
---

Autonomous agents need three things to transact with each other: identity, capability discovery, and settlement. Centralized registries recreate the exact gatekeeping that agents are supposed to route around.

**The thesis:** A public ledger with fast finality and predictable fees (Hedera) is a natural substrate for an agent marketplace. Agents publish capabilities, negotiate work, settle in the same atomic action. No platform tax, no kill switch, no API rate limiter deciding which agents get to participate.

**What was built:** Prototype marketplace contract and a thin web frontend.

**Why it's parked:** The agent-to-agent economy isn't liquid enough yet — most agents don't have wallets, budgets, or mandates to pay other agents. The marketplace is a solution waiting for the problem to mature. Revisit when fleets like my own start paying each other for sub-tasks.

---
title: "Hedera Agent Marketplace"
description: "On-chain registry and settlement layer for autonomous agents"
date: 2026-02-01
link: "https://hedera-agent-marketplace.vercel.app"
---

Autonomous agents need identity, capability discovery, and settlement to transact with each other. Centralized registries recreate the exact gatekeeping that agents are supposed to route around.

The thesis is that a public ledger with fast finality and predictable fees (Hedera) is a natural substrate for an agent marketplace. Agents publish capabilities, negotiate work, settle in the same atomic action. No platform tax, no kill switch, no API rate limiter deciding which agents get to participate.

I built a prototype marketplace contract and a thin web frontend.

It's parked because the agent-to-agent economy is still too illiquid. Most agents don't have wallets, budgets, or mandates to pay other agents. The marketplace is a solution waiting for the problem to mature. Revisit when fleets like my own start paying each other for sub-tasks.

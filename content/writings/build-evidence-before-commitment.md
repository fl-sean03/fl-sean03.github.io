---
title: "Build Evidence Before You Build Commitment"
subtitle: "A method for de-risking a project before you commit to building it"
date: 2026-07-10
---

Most technical projects don't fail because the team couldn't write enough code. They fail because an early assumption was treated as a fact.

Someone assumed a provider's interface would do what the docs implied. Someone assumed the model would hold up on the real task, not the demo one. Someone assumed a material would keep its properties at scale, or that two subsystems would talk to each other cleanly, or that a security boundary would actually hold. The team turned that assumption into a requirement, built a competent implementation around it, and only discovered the problem after the architecture was expensive to change.

The work was good. The premise was wrong. And the premise was never tested, because testing it wasn't anyone's job.

---

## The phase nobody schedules

There's a phase that belongs between having an idea and committing to build it. Not a prototype. Not a proof of concept that shows the happy path and proves nothing about failure. A short, deliberate investigation whose only purpose is to find out whether the few load-bearing assumptions are true.

I've started treating this as its own discipline, with its own rules. The core rule is a constraint on scope: don't try to prove the whole system before building it. Buy only the information you need to justify the next expensive or hard-to-reverse decision. Choosing a foundational architecture. Committing to a provider. Buying equipment. Fabricating custom hardware. Once the remaining uncertainty is ordinary implementation risk, the investigation stops and the build starts.

The discipline that makes it work is picking what to investigate. Most unknowns don't deserve an experiment. The ones that do are the ones that combine high consequence with weak evidence, that sit under the architecture, that are costly to reverse, or that a lot of other decisions depend on. Everything else is noise you'll resolve for free during development. If an experiment can't change a decision you're about to make, it's theater, and you shouldn't run it.

---

## What it looks like in practice

I ran this recently on a system I'm building that connects AI coding agents so they can hand work to each other without replacing how any of them natively work.

Before writing much, I reduced the whole thing to one sentence: connect these agents through their own interfaces without reimplementing their internals. The risky assumptions weren't the interface or the pricing. They were the boring, load-bearing ones. Could one agent's session be controlled, paused, resumed, and recovered from a crash through its native interface? Could work be handed from one to another and come back intact? And could a third agent I hadn't planned for slot into the same contract without me changing it?

So I built only enough to test those claims, and I wrote down in advance what would count as pass and fail for each one. Then I tried to break them.

The most useful result was a failure. One agent's built-in delegation could be watched but not intercepted. There was no clean way to reroute it without forking the tool itself, which wasn't worth it. On paper that sounds like bad news. It wasn't. The plan never actually needed that interception. What the failure did was retire a whole branch of the design and turn a vague worry into one precise sentence about what the product can and can't claim. A well-evidenced negative result saved me more time than a positive one would have.

The third agent slotted in with no changes to the contract. That single fact was the real proof the architecture generalized, and it cost almost nothing to get because I'd set the whole thing up to answer exactly that question.

The verdict was to proceed, with two claims kept deliberately narrow. Not "it mostly works." "It works, except here, and here's the exact wording of the limit." That distinction is the entire point.

---

## Negative results and narrow claims

Two habits do most of the work.

The first is treating a failure as a deliverable, not an embarrassment. A result that kills an approach is worth keeping, written down, with the evidence, so nobody rediscovers it in six months. Failed approaches that vanish from the record get repeated.

The second is refusing the word "mostly." Every load-bearing claim comes back as one of four things: it works as intended in a real environment, it works with a specific named limitation, it's disproven, or it's still unknown and here's the blocker. The middle option is only allowed if you write the exact constraint it puts on the product. The moment you let "works with caveats" collapse into "works," you've smuggled the risk back into the foundation you were trying to protect.

---

## Knowing when to stop

The hard part isn't starting this. It's stopping. The failure mode is that the investigation quietly becomes the product. You start polishing an interface nobody's testing. You build the general version before the second real case exists. You add the login and the billing that were never the risk. The demo becomes a maintained system without anyone deciding it should.

You're done when every project-killing assumption is either proven, bounded by a written constraint, or disproven with an accepted change of plan. When one thin path runs end to end through the real components, not mocks. When the remaining questions are the ordinary kind you answer while building. At that point more investigation isn't caution, it's avoidance.

The output isn't a demo. It's a short pile of evidence, a list of what's proven and what's only bounded, the claims you're now forbidden from making, and a build plan ordered by what's still uncertain instead of by which feature is easiest to show.

---

My broader [thesis](/writings/thesis/) is that most work dies from friction, not from being wrong. This is the same idea pointed at the beginning of a project instead of the end. The friction here is that the cheap question, "what would have to be true for this to work, and is it," gets skipped because it isn't glamorous and doesn't produce anything to show. So teams build first and find out later. The fix isn't more caution or more planning. It's a small amount of the right evidence, bought before the expensive commitment instead of after it.

I wrote up the full method, with the scoring, the templates, and the real example, as a [single reference](https://gist.github.com/fl-sean03/aabc1ab5a55b1583003765d67c55e92b).

# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=flask
actions.precombat+=/food
actions.precombat+=/augmentation
actions.precombat+=/summon_pet
actions.precombat+=/grimoire_of_sacrifice,if=talent.grimoire_of_sacrifice.enabled
actions.precombat+=/snapshot_stats
actions.precombat+=/seed_of_corruption,if=spell_targets.seed_of_corruption_aoe>=3
actions.precombat+=/haunt
actions.precombat+=/unstable_affliction

# Executed every time the actor is available.
actions=call_action_list,name=aoe,if=active_enemies>3
# Action lists for trinket behavior. Stats are saved for before Soul Rot/Impending Catastrophe/Phantom Singularity, otherwise on cooldown
actions+=/call_action_list,name=trinket_split_check,if=time<1
actions+=/call_action_list,name=delayed_trinkets
actions+=/call_action_list,name=stat_trinkets,if=(dot.soul_rot.ticking|dot.impending_catastrophe_dot.ticking|dot.phantom_singularity.ticking)&soul_shard>3|dot.vile_taint.ticking|talent.sow_the_seeds
actions+=/call_action_list,name=damage_trinkets,if=covenant.night_fae&(!variable.trinket_split|cooldown.soul_rot.remains>20|(variable.trinket_one&cooldown.soul_rot.remains<trinket.1.cooldown.remains)|(variable.trinket_two&cooldown.soul_rot.remains<trinket.2.cooldown.remains))
actions+=/call_action_list,name=damage_trinkets,if=covenant.venthyr&(!variable.trinket_split|cooldown.impending_catastrophe.remains>20|(variable.trinket_one&cooldown.impending_catastrophe.remains<trinket.1.cooldown.remains)|(variable.trinket_two&cooldown.impending_catastrophe.remains<trinket.2.cooldown.remains))
actions+=/call_action_list,name=damage_trinkets,if=(covenant.necrolord|covenant.kyrian|covenant.none)&(!variable.trinket_split|cooldown.phantom_singularity.remains>20|(variable.trinket_one&cooldown.phantom_singularity.remains<trinket.1.cooldown.remains)|(variable.trinket_two&cooldown.phantom_singularity.remains<trinket.2.cooldown.remains))
actions+=/call_action_list,name=damage_trinkets,if=!talent.phantom_singularity.enabled&(!variable.trinket_split|cooldown.summon_darkglare.remains>20|(variable.trinket_one&cooldown.summon_darkglare.remains<trinket.1.cooldown.remains)|(variable.trinket_two&cooldown.summon_darkglare.remains<trinket.2.cooldown.remains))
# Burn soul shards if fight is almost over
actions+=/malefic_rapture,if=time_to_die<execute_time*soul_shard&dot.unstable_affliction.ticking
# If covenant dot/Phantom Singularity is running, use Darkglare to extend the current set
actions+=/call_action_list,name=darkglare_prep,if=covenant.venthyr&dot.impending_catastrophe_dot.ticking&cooldown.summon_darkglare.remains<2&(dot.phantom_singularity.remains>2|!talent.phantom_singularity)
actions+=/call_action_list,name=darkglare_prep,if=covenant.night_fae&dot.soul_rot.ticking&cooldown.summon_darkglare.remains<2&(dot.phantom_singularity.remains>2|!talent.phantom_singularity)
# If using Phantom Singularity on cooldown, make sure to extend it before it runs out
actions+=/call_action_list,name=darkglare_prep,if=(covenant.necrolord|covenant.kyrian|covenant.none)&dot.phantom_singularity.ticking&dot.phantom_singularity.remains<2
# Refresh dots early if going into a shard spending phase
actions+=/call_action_list,name=dot_prep,if=covenant.night_fae&!dot.soul_rot.ticking&cooldown.soul_rot.remains<4
actions+=/call_action_list,name=dot_prep,if=covenant.venthyr&!dot.impending_catastrophe_dot.ticking&cooldown.impending_catastrophe.remains<4
actions+=/call_action_list,name=dot_prep,if=(covenant.necrolord|covenant.kyrian|covenant.none)&talent.phantom_singularity&!dot.phantom_singularity.ticking&cooldown.phantom_singularity.remains<4
# If Phantom Singularity is ticking, it is safe to use Dark Soul
actions+=/dark_soul,if=dot.phantom_singularity.ticking
actions+=/dark_soul,if=!talent.phantom_singularity&(dot.soul_rot.ticking|dot.impending_catastrophe_dot.ticking)
# Sync Phantom Singularity with Venthyr/Night Fae covenant dot, otherwise use on cooldown. If Empyreal Ordnance buff is incoming, hold until it's ready (18 seconds after use)
actions+=/phantom_singularity,if=covenant.night_fae&time>5&cooldown.soul_rot.remains<1&(trinket.empyreal_ordnance.cooldown.remains<162|!equipped.empyreal_ordnance)
actions+=/phantom_singularity,if=covenant.venthyr&time>5&cooldown.impending_catastrophe.remains<1&(trinket.empyreal_ordnance.cooldown.remains<162|!equipped.empyreal_ordnance)
actions+=/phantom_singularity,if=(covenant.necrolord|covenant.kyrian|covenant.none)&(trinket.empyreal_ordnance.cooldown.remains<162|!equipped.empyreal_ordnance)
actions+=/phantom_singularity,if=time_to_die<16
# If Phantom Singularity is ticking, it's time to use other major dots
actions+=/call_action_list,name=covenant,if=dot.phantom_singularity.ticking&(covenant.night_fae|covenant.venthyr)
actions+=/agony,cycle_targets=1,target_if=dot.agony.remains<4
actions+=/haunt
# Sow the Seeds on 3 targets if it isn't currently in flight or on the target. With Siphon Life it's also better to use Seed over manually applying 3 Corruptions.
actions+=/seed_of_corruption,if=active_enemies>2&talent.sow_the_seeds&!dot.seed_of_corruption.ticking&!in_flight
actions+=/seed_of_corruption,if=active_enemies>2&talent.siphon_life&!dot.seed_of_corruption.ticking&!in_flight&dot.corruption.remains<4
actions+=/vile_taint,if=(soul_shard>1|active_enemies>2)&cooldown.summon_darkglare.remains>12
actions+=/unstable_affliction,if=dot.unstable_affliction.remains<4
actions+=/siphon_life,cycle_targets=1,target_if=dot.siphon_life.remains<4
# If not using Phantom Singularity, don't apply covenant dots until other core dots are safe
actions+=/call_action_list,name=covenant,if=!covenant.necrolord
# Apply Corruption manually on 1-2 targets, or on 3 with Absolute Corruption
actions+=/corruption,cycle_targets=1,if=active_enemies<4-(talent.sow_the_seeds|talent.siphon_life),target_if=dot.corruption.remains<2
# After the opener, spend a shard when at 5 on Malefic Rapture to avoid overcapping
actions+=/malefic_rapture,if=soul_shard>4&time>21
# When not syncing Phantom Singularity to Venthyr/Night Fae, Summon Darkglare if all dots are applied
actions+=/call_action_list,name=darkglare_prep,if=covenant.venthyr&!talent.phantom_singularity&dot.impending_catastrophe_dot.ticking&cooldown.summon_darkglare.ready
actions+=/call_action_list,name=darkglare_prep,if=covenant.night_fae&!talent.phantom_singularity&dot.soul_rot.ticking&cooldown.summon_darkglare.ready
actions+=/call_action_list,name=darkglare_prep,if=(covenant.necrolord|covenant.kyrian|covenant.none)&cooldown.summon_darkglare.ready
# Use Dark Soul if Darkglare won't be ready again, or if there will be at least 2 more Darkglare uses
actions+=/dark_soul,if=cooldown.summon_darkglare.remains>time_to_die&(!talent.phantom_singularity|cooldown.phantom_singularity.remains>time_to_die)
actions+=/dark_soul,if=!talent.phantom_singularity&cooldown.summon_darkglare.remains+cooldown.summon_darkglare.duration<time_to_die
# Catch-all item usage for anything not specified elsewhere
actions+=/call_action_list,name=item
# Refresh Shadow Embrace before spending shards on Malefic Rapture
actions+=/call_action_list,name=se,if=debuff.shadow_embrace.stack<(2-action.shadow_bolt.in_flight)|debuff.shadow_embrace.remains<3
# Use Malefic Rapture when major dots are up, or if there will be significant time until the next Phantom Singularity
actions+=/malefic_rapture,if=dot.vile_taint.ticking|dot.impending_catastrophe_dot.ticking|dot.soul_rot.ticking
actions+=/malefic_rapture,if=talent.phantom_singularity&(dot.phantom_singularity.ticking|cooldown.phantom_singularity.remains>25|time_to_die<cooldown.phantom_singularity.remains)
actions+=/malefic_rapture,if=talent.sow_the_seeds
# Drain Life is only a DPS gain with Inevitable Demise near max stacks. If fight is about to end do not miss spending the stacks
actions+=/drain_life,if=buff.inevitable_demise.stack>40|buff.inevitable_demise.up&time_to_die<4
actions+=/call_action_list,name=covenant
actions+=/agony,cycle_targets=1,target_if=refreshable
actions+=/unstable_affliction,if=refreshable
actions+=/siphon_life,cycle_targets=1,target_if=refreshable
actions+=/corruption,cycle_targets=1,if=active_enemies<4-(talent.sow_the_seeds|talent.siphon_life),target_if=refreshable
actions+=/drain_soul,interrupt=1
actions+=/shadow_bolt

actions.aoe=phantom_singularity
actions.aoe+=/haunt
actions.aoe+=/call_action_list,name=darkglare_prep,if=covenant.venthyr&dot.impending_catastrophe_dot.ticking&cooldown.summon_darkglare.ready&(dot.phantom_singularity.remains>2|!talent.phantom_singularity)
actions.aoe+=/call_action_list,name=darkglare_prep,if=covenant.night_fae&dot.soul_rot.ticking&cooldown.summon_darkglare.ready&(dot.phantom_singularity.remains>2|!talent.phantom_singularity)
actions.aoe+=/call_action_list,name=darkglare_prep,if=(covenant.necrolord|covenant.kyrian|covenant.none)&dot.phantom_singularity.ticking&dot.phantom_singularity.remains<2
actions.aoe+=/seed_of_corruption,if=talent.sow_the_seeds&can_seed
actions.aoe+=/seed_of_corruption,if=!talent.sow_the_seeds&!dot.seed_of_corruption.ticking&!in_flight&dot.corruption.refreshable
actions.aoe+=/agony,cycle_targets=1,if=active_dot.agony<4,target_if=!dot.agony.ticking
actions.aoe+=/agony,cycle_targets=1,if=active_dot.agony>=4,target_if=refreshable&dot.agony.ticking
actions.aoe+=/unstable_affliction,if=dot.unstable_affliction.refreshable
actions.aoe+=/vile_taint,if=soul_shard>1
actions.aoe+=/call_action_list,name=covenant,if=!covenant.necrolord
actions.aoe+=/call_action_list,name=darkglare_prep,if=covenant.venthyr&(cooldown.impending_catastrophe.ready|dot.impending_catastrophe_dot.ticking)&cooldown.summon_darkglare.ready&(dot.phantom_singularity.remains>2|!talent.phantom_singularity)
actions.aoe+=/call_action_list,name=darkglare_prep,if=(covenant.necrolord|covenant.kyrian|covenant.none)&cooldown.summon_darkglare.remains<2&(dot.phantom_singularity.remains>2|!talent.phantom_singularity)
actions.aoe+=/call_action_list,name=darkglare_prep,if=covenant.night_fae&(cooldown.soul_rot.ready|dot.soul_rot.ticking)&cooldown.summon_darkglare.remains<2&(dot.phantom_singularity.remains>2|!talent.phantom_singularity)
actions.aoe+=/dark_soul,if=cooldown.summon_darkglare.remains>time_to_die&(!talent.phantom_singularity|cooldown.phantom_singularity.remains>time_to_die)
actions.aoe+=/dark_soul,if=cooldown.summon_darkglare.remains+cooldown.summon_darkglare.duration<time_to_die
actions.aoe+=/call_action_list,name=item
actions.aoe+=/call_action_list,name=delayed_trinkets
actions.aoe+=/call_action_list,name=damage_trinkets
actions.aoe+=/call_action_list,name=stat_trinkets,if=dot.phantom_singularity.ticking|!talent.phantom_singularity
actions.aoe+=/malefic_rapture,if=dot.vile_taint.ticking
actions.aoe+=/malefic_rapture,if=dot.soul_rot.ticking&!talent.sow_the_seeds
actions.aoe+=/malefic_rapture,if=!talent.vile_taint
actions.aoe+=/malefic_rapture,if=soul_shard>4
actions.aoe+=/siphon_life,cycle_targets=1,if=active_dot.siphon_life<=3,target_if=!dot.siphon_life.ticking
actions.aoe+=/call_action_list,name=covenant
actions.aoe+=/drain_life,if=buff.inevitable_demise.stack>=50|buff.inevitable_demise.up&time_to_die<5|buff.inevitable_demise.stack>=35&dot.soul_rot.ticking
actions.aoe+=/drain_soul,interrupt=1
actions.aoe+=/shadow_bolt

actions.covenant=impending_catastrophe,if=!talent.phantom_singularity&(cooldown.summon_darkglare.remains<10|cooldown.summon_darkglare.remains>50&cooldown.summon_darkglare.remains>25&conduit.corrupting_leer)
actions.covenant+=/impending_catastrophe,if=talent.phantom_singularity&dot.phantom_singularity.ticking
actions.covenant+=/decimating_bolt,if=cooldown.summon_darkglare.remains>5&(debuff.haunt.remains>4|!talent.haunt)
actions.covenant+=/soul_rot,if=!talent.phantom_singularity&(cooldown.summon_darkglare.remains<5|cooldown.summon_darkglare.remains>50|cooldown.summon_darkglare.remains>25&conduit.corrupting_leer)
actions.covenant+=/soul_rot,if=talent.phantom_singularity&dot.phantom_singularity.ticking
actions.covenant+=/scouring_tithe

actions.damage_trinkets=use_item,name=soul_igniter
actions.damage_trinkets+=/use_item,name=dreadfire_vessel
actions.damage_trinkets+=/use_item,name=glyph_of_assimilation

actions.darkglare_prep=vile_taint
actions.darkglare_prep+=/dark_soul
actions.darkglare_prep+=/potion
actions.darkglare_prep+=/fireblood
actions.darkglare_prep+=/blood_fury
actions.darkglare_prep+=/berserking
actions.darkglare_prep+=/call_action_list,name=covenant,if=!covenant.necrolord
actions.darkglare_prep+=/summon_darkglare

actions.delayed_trinkets=use_item,name=empyreal_ordnance,if=(covenant.night_fae&cooldown.soul_rot.remains<20)|(covenant.venthyr&cooldown.impending_catastrophe.remains<20)|(covenant.necrolord|covenant.kyrian|covenant.none)
actions.delayed_trinkets+=/use_item,name=sunblood_amethyst,if=(covenant.night_fae&cooldown.soul_rot.remains<6)|(covenant.venthyr&cooldown.impending_catastrophe.remains<6)|(covenant.necrolord|covenant.kyrian|covenant.none)
actions.delayed_trinkets+=/use_item,name=soulletting_ruby,if=(covenant.night_fae&cooldown.soul_rot.remains<8)|(covenant.venthyr&cooldown.impending_catastrophe.remains<8)|(covenant.necrolord|covenant.kyrian|covenant.none)

actions.dot_prep=agony,if=dot.agony.remains<8&cooldown.summon_darkglare.remains>dot.agony.remains
actions.dot_prep+=/siphon_life,if=dot.siphon_life.remains<8&cooldown.summon_darkglare.remains>dot.siphon_life.remains
actions.dot_prep+=/unstable_affliction,if=dot.unstable_affliction.remains<8&cooldown.summon_darkglare.remains>dot.unstable_affliction.remains
actions.dot_prep+=/corruption,if=dot.corruption.remains<8&cooldown.summon_darkglare.remains>dot.corruption.remains

actions.item=use_items

actions.se=haunt
actions.se+=/drain_soul,interrupt_global=1,interrupt_if=debuff.shadow_embrace.stack>=3
actions.se+=/shadow_bolt

actions.stat_trinkets=use_item,name=inscrutable_quantum_device
actions.stat_trinkets+=/use_item,name=instructors_divine_bell
actions.stat_trinkets+=/use_item,name=overflowing_anima_cage
actions.stat_trinkets+=/use_item,name=darkmoon_deck_putrescence
actions.stat_trinkets+=/use_item,name=macabre_sheet_music
actions.stat_trinkets+=/use_item,name=flame_of_battle
actions.stat_trinkets+=/use_item,name=wakeners_frond
actions.stat_trinkets+=/use_item,name=tablet_of_despair
actions.stat_trinkets+=/use_item,name=sinful_aspirants_badge_of_ferocity
actions.stat_trinkets+=/use_item,name=sinful_gladiators_badge_of_ferocity
actions.stat_trinkets+=/blood_fury
actions.stat_trinkets+=/fireblood
actions.stat_trinkets+=/berserking

actions.trinket_split_check=variable,name=special_equipped,value=(((equipped.empyreal_ordnance^equipped.inscrutable_quantum_device)^equipped.soulletting_ruby)^equipped.sunblood_amethyst)
actions.trinket_split_check+=/variable,name=trinket_one,value=(trinket.1.has_proc.any&trinket.1.has_cooldown)
actions.trinket_split_check+=/variable,name=trinket_two,value=(trinket.2.has_proc.any&trinket.2.has_cooldown)
actions.trinket_split_check+=/variable,name=damage_trinket,value=(!(trinket.1.has_proc.any&trinket.1.has_cooldown))|(!(trinket.2.has_proc.any&trinket.2.has_cooldown))|equipped.glyph_of_assimilation
actions.trinket_split_check+=/variable,name=trinket_split,value=(variable.trinket_one&variable.damage_trinket)|(variable.trinket_two&variable.damage_trinket)|(variable.trinket_one^variable.special_equipped)|(variable.trinket_two^variable.special_equipped)

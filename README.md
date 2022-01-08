Partial Cell Availability for gNodeB Cell	NR	AVAILABILITY	1	N19Q4.1	GNBDUFunction	NRCellDU	SINGLE	PERCENTAGE	PRELIMINARY	"Measures percentage of time when a cell is available for service defined as availability. Cell availability for a cluster of CELL number of cells during Reporting Periods (ROPs) can be calculated using below formula. KPI has following features: -- This KPI measures system performance. -- Metric shows higher benefit when metric value is higher. -- Since measured by gNodeB, KPI does not include time when gNodeB is down. That is, node restart time is excluded. -- Percentage of time when a cell is available for service is defined as cell availability. -- KPI is on NRCellDU level.
"	"Manual blocking time of a cell is included in this KPI to show overall availability of cell. To remove manual intervention impact on cell availability, remove pmCellDowntimeMan from numerator and subtract value of pmCellDowntimeMan from denominator.
If files with PM counters are missing, time that those files represent in ROPxCELLx900 can be excluded from Cell Availability result.
Default setting for delay timer is 0, which does not affect cell restart time. If delay timer is set to be larger than 0, cell restart or unlock time duration is extended as a consequence of number of TX updates taken place during lock or unlock procedure.
"	[{'Name': 'pmCellDowntimeAuto', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmCellDowntimeMan', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	100 * (ROP * CELL * 900 - sum_over_elements<CELL,ROP>(pmCellDowntimeAuto + pmCellDowntimeMan)) / (ROP * CELL * 900)
Average DL MAC Cell Throughput - fixed time normalized	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"-- Throughput achieved by total DL MAC volume during a complete measurement period (ROP).
-- Metric shows higher benefit when metric value is higher.
-- PM counter in this KPI is on cell level.
"	"-- pmMacVolDl is at MAC layer to measure MAC PDU volume and includes both PCell and SCell traffic if Carrier Aggregation is active.
"	[{'Name': 'pmMacVolDl', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	(8 * pmMacVolDl) / (900 * 1000)
Average DL MAC DRB Latency per QoS covering DRX In-sync	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	ARRAY	MILLI_SECONDS	PRELIMINARY	"-- DL MAC DRB latency can further be differentiated on UE DRX and UL synchronization states.
-- Different latency counters are incremented depending on which DRX and UL synchronization state the burst starts in.
-- Average DRB latency for bursts that start in DRX-Sleep State and given by UL-In-Sync state.
-- This KPI measures impact on end user.
-- PM counters in this KPI are on cell level.
"	"--
"	[{'Name': 'pmMacLatTimeDlDrxSyncQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}, {'Name': 'pmMacLatTimeDlDrxSyncSampQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}]	(pmMacLatTimeDlDrxSyncQos[$input] / 8) / pmMacLatTimeDlDrxSyncSampQos[$input]
Average DL MAC DRB Latency per QoS covering non-DRX In-sync	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	ARRAY	MILLI_SECONDS	PRELIMINARY	"-- DL MAC DRB latency can further be differentiated on UE DRX and UL synchronization states.
-- Different latency counters are incremented depending on which DRX and UL synchronization state the burst starts in.
-- Average DRB latency for bursts that start in DRX-Awake state and given by UL-In-Sync state.
-- This KPI measures impact on end user.
-- PM counters in this KPI are on cell level.
"	"--
"	[{'Name': 'pmMacLatTimeDlNoDrxSyncQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}, {'Name': 'pmMacLatTimeDlNoDrxSyncSampQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}]	(pmMacLatTimeDlNoDrxSyncQos[$input] / 8) / pmMacLatTimeDlNoDrxSyncSampQos[$input]
Average DL MAC DRB Throughput	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"-- Shows DRB DL throughput for data bursts that are restricted by air interface.
-- Single burst and contribution from last slot are not considered.
-- This KPI measures impact on end user.
-- Metric shows higher benefit when metric value is higher.
-- PM counters in this KPI are on cell level.
"	"-- Compared to 3GPP 28.554 definition of the KPI:
   This KPI measures MAC level volume instead of RLC level.
"	[{'Name': 'pmMacVolDlDrb', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmMacTimeDlDrb', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	64 * (pmMacVolDlDrb / pmMacTimeDlDrb)
![image](https://user-images.githubusercontent.com/72145932/148649563-2445c11e-ccf1-42ac-a9a7-be0158051508.png)

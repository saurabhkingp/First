Name	NeType	Category	SchemaVersion	LastModified	NetworkFunction	Level	FormulaResult	FormulaUnit	FormulaStatus	Description	Notes	Counters	Formula
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
Average Overall DL Latency	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	ARRAY	MILLI_SECONDS	PRELIMINARY	"-- This KPI measures impact on end user.
-- PM counters in this KPI are on cell level.
"	"-- Compared to 3GPP 28.554 definition of the KPI:
   This KPI measures MAC level volume instead of RLC level.

-- Latency will increase with more instantaneously active UEs and will also depend on the scheduling algorithm(s) being used and on DRX state, especially for the specific QoS.
"	[{'Name': 'pmMacLatTimeDlNoDrxSyncQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}, {'Name': 'pmMacLatTimeDlDrxSyncQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}, {'Name': 'pmMacLatTimeDlNoDrxSyncSampQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}, {'Name': 'pmMacLatTimeDlDrxSyncSampQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}]	((pmMacLatTimeDlNoDrxSyncQos[$input] + pmMacLatTimeDlDrxSyncQos[$input]) / 8) / (pmMacLatTimeDlNoDrxSyncSampQos[$input] + pmMacLatTimeDlDrxSyncSampQos[$input])
Average UL MAC Cell Throughput - fixed time normalized	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"-- Throughput achieved by total UL MAC volume during a complete measurement period (ROP).
-- Metric shows higher benefit when metric value is higher.
-- PM counter in this KPI is on cell level.
"	"-- pmMacVolUl is at MAC layer and includes both PCell and SCell traffic if UL CA is active.
"	[{'Name': 'pmMacVolUl', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	(8 * pmMacVolUl) / (900 * 1000)
Average UL MAC UE Throughput	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"Following equation gives UL MAC UE throughput for data bursts restricted by air interface.
-- This KPI measures the impact on end user.
-- Metric shows higher benefit when metric value is higher.
-- PM counters in this KPI are on cell level.
"	"-- Compared to 3GPP 28.554 definition of the KPI:
   This KPI measures MAC level volume instead of RLC level.
"	[{'Name': 'pmMacVolUlResUe', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmMacTimeUlResUe', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	64 * (pmMacVolUlResUe / pmMacTimeUlResUe)
DL MAC DRB Throughput per QoS	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	ARRAY	KILO_BITS_PER_SECOND	PRELIMINARY	"-- For each QoS class, such as 5QI or QCI, shows DRB DL throughput for data bursts restricted by air interface.
-- Single burst and contribution from last slot are not considered.
-- This KPI measures impact on end user.
-- Metric shows higher benefit when metric value is higher.
-- PM counters in this KPI are on cell level.
"	"-- Compared to 3GPP 28.554 definition of the KPI:
   This KPI measures MAC level volume instead of RLC level.
"	[{'Name': 'pmMacVolDlDrbQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}, {'Name': 'pmMacTimeDlDrbQos', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 256, 'Compressed': True}]	64 * (pmMacVolDlDrbQos[$input] / pmMacTimeDlDrbQos[$input])
Normalized Average DL MAC Cell Throughput considering traffic	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"-- Normalized throughput against traffic. Slots where no traffic is taking place are excluded.
-- Metric shows higher benefit when metric value is higher.
-- PM counters in this KPI are on cell level.
"	"-- pmMacVolDl is at MAC layer to measure MAC PDU volume and includes both PCell and SCell traffic if Carrier Aggregation is active.
"	[{'Name': 'pmMacVolDl', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmPdschSchedActivity', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	64 * (pmMacVolDl / pmPdschSchedActivity)
Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"-- Normalized throughput against traffic. Slots where no traffic is taking place are excluded. Only slots where PUSCH can be decoded for any UE are included.
-- Metric shows higher benefit when metric value is higher.
-- PM counters in this KPI are on cell level.
"	"-- pmMacVolUl is at MAC layer and includes both PCell and SCell traffic if UL CA is active.
"	[{'Name': 'pmMacVolUl', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmPuschSchedActivity', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	64 * (pmMacVolUl / pmPuschSchedActivity)
Normalized DL MAC Cell Throughput considering actual PDSCH slot only	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"-- KPI is normalized for TDD pattern so that only time available for DL is included.
-- Metric shows higher benefit when metric value is higher.
-- PM counters in this KPI are on cell level.
"	"-- pmMacVolDl is at MAC layer to measure MAC PDU volume and includes both PCell and SCell traffic if Carrier Aggregation is active.
"	[{'Name': 'pmMacVolDl', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmPdschAvailTime', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	64 * (pmMacVolDl / pmPdschAvailTime)
Normalized UL MAC Cell Throughput considering actual PUSCH slot only	NR	INTEGRITY	1	N19Q2.1	GNBDUFunction	NRCellDU	SINGLE	KILO_BITS_PER_SECOND	PRELIMINARY	"-- KPI is normalized for TDD pattern so that only time available for UL is included. All PUSCH slots are considered whether decoded, not decoded, or unused.
-- Metric shows higher benefit when metric value is higher.
-- PM counters in this KPI are on cell level.
"	"-- pmMacVolUl is at MAC layer and includes both PCell and SCell traffic if UL CA is active.
"	[{'Name': 'pmMacVolUl', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmPuschAvailTime', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	64 * (pmMacVolUl / pmPuschAvailTime)
Random Access Success Rate Captured in gNodeB	NR_NSA	ACCESSIBILITY	1	N19Q4.2	GNBDUFunction	NRCellDU	SINGLE	PERCENTAGE	PRELIMINARY	"The frequency of receiving a Random Access Message 3 (RaMsg3) after transmitting a Random Access Message 2 (RaMsg2).
KPI has following features:
-- This KPI measures impact on end user.
-- Metric shows higher benefit when metric value is higher.
-- KPI is on NRCellDU level.
"		[{'Name': 'pmRadioRaCbAttMsg2', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmRadioRaCbSuccMsg3', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	100 * (pmRadioRaCbSuccMsg3 / pmRadioRaCbAttMsg2)
CBRA Success Rate	NR_SA	ACCESSIBILITY	1	N19Q4.2	GNBDUFunction	NRCellDU	SINGLE	PERCENTAGE	PRELIMINARY	"Aggregation over multiple ROPs and MOs shall be the sum of pmCounters at the numerator divided by the sum of the counters at the denominator and multiplied by 100.
"		[{'Name': 'pmRadioRaCbSuccMsg3', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}, {'Name': 'pmRadioRaCbPreambles', 'MoClasses': ['NRCellDU'], 'Flex': False, 'ArraySize': 1, 'Compressed': False}]	100 * (pmRadioRaCbSuccMsg3 / pmRadioRaCbPreambles)
![image](https://user-images.githubusercontent.com/72145932/148650505-68f02bb8-35a6-42e3-84ce-b1d56b5dabc8.png)

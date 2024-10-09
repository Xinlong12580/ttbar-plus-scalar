from ttbarphiclass import *
from TIMBER.Tools.Common import CompileCpp 
CompileCpp("ttbarphimodules.cc")
testins=ttbarphiClass("root://cmsxrootd.fnal.gov//store/mc/RunIISummer20UL16NanoAODv9/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F43B5F34-8F07-9A41-8F2F-8E14828E585F.root",17,1,60)
testins.ApplyStandardCorrections()
testins.Preselection()
testins.Selection()
testins.JetsCandidateKinematicinfo()
testins.MassReconstruction()
testins.Snapshot()
#testins.Snapshot()

#testins.a.Snapshot(['LeptonTestAndReOrdering'], 'test_output.root', 'Events', openOption='RECREATE', saveRunChain=True)


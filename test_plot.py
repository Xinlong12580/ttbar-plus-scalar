import ROOT
ROOT.gROOT.SetBatch(True)
rdf=ROOT.RDataFrame("Events","ttbarphisnapshot_F43B5F34-8F07-9A41-8F2F-8E14828E585F.root_17_1of60.root")
hinvmass=rdf.Histo1D(("inv_mass","inv_mass",10,0,10),"PhiInvMass")
ca=ROOT.TCanvas('c','c')
hinvmass.Draw()
ca.Print("hinvmass.pdf")
